#!/usr/bin/env bash
# Prune Vercel deployments to free Hobby Disk Size (~10 GB).
# 1) Optionally deletes orphan projects (no custom domain / superseded)
# 2) Keeps the N newest production deployments per project; deletes the rest
#    (and all ERROR/CANCELED). Retries on HTTP 429.
#
# Usage:
#   VERCEL_TOKEN=... bash scripts/prune-vercel-disk.sh
#   VERCEL_TOKEN=... bash scripts/prune-vercel-disk.sh --delete-orphans
#   VERCEL_TOKEN=... bash scripts/prune-vercel-disk.sh --dry-run
set -euo pipefail

KEEP_PROD="${KEEP_PROD:-5}"
DRY_RUN=0
DELETE_ORPHANS=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    --delete-orphans) DELETE_ORPHANS=1 ;;
  esac
done

if [[ -z "${VERCEL_TOKEN:-}" ]]; then
  for f in \
    "${HOME}/APP Eventi da GAS/.env.local" \
    "/Users/mauroandreoni/APP Eventi da GAS/.env.local"
  do
    if [[ -f "$f" ]]; then
      VERCEL_TOKEN="$(grep -E '^[[:space:]]*VERCEL_TOKEN=' "$f" | tail -1 | sed -E 's/^[[:space:]]*VERCEL_TOKEN=//' | tr -d '\r' | sed 's/^["'\'']//;s/["'\'']$//' | sed 's/[[:space:]]*$//')"
      [[ -n "$VERCEL_TOKEN" ]] && break
    fi
  done
fi
[[ -n "${VERCEL_TOKEN:-}" ]] || { echo "Missing VERCEL_TOKEN" >&2; exit 1; }

export VERCEL_TOKEN KEEP_PROD DRY_RUN DELETE_ORPHANS
python3 <<'PY'
import json, os, time, urllib.request, urllib.error, re

token = os.environ["VERCEL_TOKEN"]
keep = int(os.environ.get("KEEP_PROD", "5"))
dry = os.environ.get("DRY_RUN") == "1"
delete_orphans = os.environ.get("DELETE_ORPHANS") == "1"
ORPHAN_NAMES = {"web", "musicpro-eventi-web", "app-eventi-iumu"}

def api(method, path, data=None, retries=8):
    body = None if data is None else json.dumps(data).encode()
    for attempt in range(retries):
        req = urllib.request.Request(
            f"https://api.vercel.com{path}",
            data=body,
            method=method,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req) as resp:
                raw = resp.read().decode() or "{}"
                return json.loads(raw) if raw.strip() else {}
        except urllib.error.HTTPError as e:
            err = e.read().decode()
            if e.code == 429:
                wait = 60
                m = re.search(r"try again in (\d+) minutes?", err)
                if m:
                    wait = int(m.group(1)) * 60 + 15
                m2 = re.search(r'"reset":\s*(\d+)', err)
                if m2:
                    reset = int(m2.group(1)) / 1000.0
                    wait = max(wait, int(reset - time.time()) + 5)
                print(f"  rate limited — sleep {wait}s (attempt {attempt+1}/{retries})")
                time.sleep(max(wait, 5))
                continue
            raise SystemExit(f"{method} {path} → {e.code}: {err[:400]}")
    raise SystemExit(f"{method} {path} → still rate limited after retries")

projects = api("GET", "/v9/projects?limit=100").get("projects", [])
deleted = 0

if delete_orphans:
    print("== orphan projects (first) ==")
    for p in list(projects):
        name = p["name"]
        if name not in ORPHAN_NAMES:
            continue
        link = p.get("link") or {}
        if name == "app-eventi-iumu" or not link.get("repo"):
            pid = p["id"]
            if dry:
                print(f"  dry-run DELETE project {name} ({pid})")
            else:
                api("DELETE", f"/v9/projects/{pid}")
                print(f"  deleted project {name}")
                deleted += 1
    projects = api("GET", "/v9/projects?limit=100").get("projects", [])

for p in projects:
    name = p["name"]
    pid = p["id"]
    deps = api("GET", f"/v6/deployments?projectId={pid}&limit=100").get("deployments", [])
    deps.sort(key=lambda d: d.get("created") or 0, reverse=True)
    prod = [d for d in deps if d.get("target") == "production"]

    keep_ids = {d["uid"] for d in prod[:keep]}
    if deps:
        keep_ids.add(deps[0]["uid"])

    to_delete = []
    for d in deps:
        uid = d["uid"]
        state = (d.get("state") or d.get("readyState") or "").upper()
        if uid in keep_ids:
            continue
        if state in ("ERROR", "CANCELED", "CANCELLED"):
            to_delete.append(d)
        elif d.get("target") != "production":
            to_delete.append(d)
        elif d not in prod[:keep]:
            to_delete.append(d)

    print(f"\n== {name}: {len(deps)} listed, keep prod≤{keep}, delete {len(to_delete)}")
    for d in to_delete:
        uid = d["uid"]
        state = d.get("state") or d.get("readyState")
        if dry:
            print(f"  dry-run DELETE {uid} {state} {d.get('url')}")
        else:
            api("DELETE", f"/v13/deployments/{uid}")
            print(f"  deleted {uid} {state}")
            deleted += 1
            time.sleep(0.15)  # gentle pacing

# Tighten retention so Disk Size does not refill
print("\n== tighten deploymentExpiration (keep=5, days=14) ==")
for p in projects:
    pid = p["id"]
    name = p["name"]
    payload = {
        "deploymentExpiration": {
            "expirationDays": 14,
            "expirationDaysProduction": 14,
            "expirationDaysCanceled": 7,
            "expirationDaysErrored": 7,
            "deploymentsToKeep": 5,
        }
    }
    if dry:
        print(f"  dry-run PATCH {name}")
    else:
        api("PATCH", f"/v9/projects/{pid}", payload)
        print(f"  patched {name}")

print(f"\nDone. deleted_ops≈{deleted} dry_run={dry}")
PY
