/**
 * Modalità Revisione — selezione Pencil + menu contestuale + edit a mano.
 * Solo su elefranco-lettura.html (reader-mode). Persistenza in localStorage.
 * Le patch vanno in revisioni.json via preview.py; i file Python restano la fonte.
 */
(function () {
  "use strict";

  if (!document.body.classList.contains("reader-mode")) return;

  var STORAGE_KEY = "elefranco-revisioni-v1";
  var UNDO_LIMIT = 20;
  var HINT_MS = 7000;
  var LONG_PRESS_MS = 450;

  var active = false;
  var editing = false;
  var lastPointerType = "mouse";
  var longPressTimer = null;
  var longPressTarget = null;
  var suppressSync = false;
  var syncTimer = null;
  var serverOnline = false;
  var hintTimer = null;
  var undoStack = [];
  var selSnap = null;
  var tempSelect = null;

  function loadAll() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
    } catch (e) {
      return {};
    }
  }

  function saveAll(data) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    if (!suppressSync) scheduleSync();
  }

  function episodeKey(ep) {
    return String(ep);
  }

  function uuid() {
    return "r" + Date.now().toString(36) + Math.random().toString(36).slice(2, 8);
  }

  function normalizeSpace(s) {
    return String(s || "").replace(/\s+/g, " ").trim();
  }

  function episodeTitle(episodeEl) {
    var h = episodeEl.querySelector(".episode-title");
    return h ? h.textContent.trim() : "Episodio " + episodeEl.dataset.episode;
  }

  function findEpisode(node) {
    var el = node && node.nodeType === Node.ELEMENT_NODE ? node : node && node.parentElement;
    while (el) {
      if (el.classList && el.classList.contains("episode") && el.dataset.episode) return el;
      el = el.parentElement;
    }
    return null;
  }

  function findEditableRoot(node) {
    var el = node && (node.nodeType === Node.ELEMENT_NODE ? node : node.parentElement);
    while (el) {
      if (el.classList) {
        if (el.classList.contains("story-text")) return el;
        if (el.classList.contains("schema")) return el;
        if (el.classList.contains("episode-title")) return el;
        if (el.classList.contains("color-hint")) return el;
      }
      el = el.parentElement;
    }
    return null;
  }

  function describeTarget(root) {
    if (!root) return { target: "racconto", field: "" };
    if (root.classList.contains("story-text")) return { target: "racconto", field: "" };
    if (root.classList.contains("schema")) return { target: "schema", field: "" };
    if (root.classList.contains("episode-title")) return { target: "title", field: "" };
    if (root.classList.contains("color-hint")) return { target: "hint", field: "" };
    return { target: "altro", field: "" };
  }

  function fieldFromRange(range) {
    var node = range && range.commonAncestorContainer;
    var el = node && (node.nodeType === Node.ELEMENT_NODE ? node : node.parentElement);
    var row = el && el.closest && el.closest(".schema-row");
    if (!row) return "";
    var label = row.querySelector(".schema-label");
    return label ? normalizeSpace(label.textContent).replace(/:$/, "") : "";
  }

  function editableRoots(episodeEl) {
    return {
      racconto: episodeEl.querySelector(".story-text"),
      schema: episodeEl.querySelector(".schema"),
      title: episodeEl.querySelector(".episode-title"),
      hint: episodeEl.querySelector(".color-hint"),
    };
  }

  function rootForTarget(episodeEl, target) {
    var roots = editableRoots(episodeEl);
    return roots[target] || roots.racconto;
  }

  function textNodesIn(root) {
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        if (!node.nodeValue || !node.nodeValue.length) return NodeFilter.FILTER_REJECT;
        var p = node.parentElement;
        if (p && p.classList.contains("revision-mark")) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      },
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    return nodes;
  }

  function rangeFromOffsets(root, start, end) {
    var nodes = textNodesIn(root);
    var pos = 0;
    var startNode = null;
    var startOff = 0;
    var endNode = null;
    var endOff = 0;

    for (var i = 0; i < nodes.length; i++) {
      var len = nodes[i].nodeValue.length;
      if (startNode === null && pos + len >= start) {
        startNode = nodes[i];
        startOff = start - pos;
      }
      if (endNode === null && pos + len >= end) {
        endNode = nodes[i];
        endOff = end - pos;
        break;
      }
      pos += len;
    }

    if (!startNode || !endNode) return null;
    var range = document.createRange();
    range.setStart(startNode, startOff);
    range.setEnd(endNode, endOff);
    return range;
  }

  function offsetsFromRange(root, range) {
    var pre = document.createRange();
    pre.selectNodeContents(root);
    pre.setEnd(range.startContainer, range.startOffset);
    var start = pre.toString().length;
    pre.setEnd(range.endContainer, range.endOffset);
    var end = pre.toString().length;
    return { start: start, end: end, text: range.toString() };
  }

  function findTextRange(root, text) {
    if (!text) return null;
    var plain = root.textContent;
    var idx = plain.indexOf(text);
    if (idx < 0) return null;
    return rangeFromOffsets(root, idx, idx + text.length);
  }

  function wrapTextNode(node, id, note) {
    var mark = document.createElement("mark");
    mark.className = "revision-mark";
    mark.dataset.revisionId = id;
    if (note) mark.dataset.revisionNote = note;
    node.parentNode.insertBefore(mark, node);
    mark.appendChild(node);
    return mark;
  }

  function splitAndWrap(node, start, end, id, note) {
    var text = node.nodeValue;
    var before = text.slice(0, start);
    var middle = text.slice(start, end);
    var after = text.slice(end);
    var parent = node.parentNode;

    if (before) parent.insertBefore(document.createTextNode(before), node);
    var midNode = document.createTextNode(middle);
    wrapTextNode(midNode, id, note);
    if (after) parent.insertBefore(document.createTextNode(after), node);
    parent.removeChild(node);
  }

  function applyRangeHighlight(range, id, note) {
    var nodes = [];
    var walker = document.createTreeWalker(range.commonAncestorContainer, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!range.intersectsNode(n)) return NodeFilter.FILTER_REJECT;
        if (n.parentElement && n.parentElement.classList.contains("revision-mark")) {
          return NodeFilter.FILTER_REJECT;
        }
        return NodeFilter.FILTER_ACCEPT;
      },
    });
    while (walker.nextNode()) nodes.push(walker.currentNode);

    nodes.forEach(function (node) {
      var start = 0;
      var end = node.nodeValue.length;
      if (node === range.startContainer) start = range.startOffset;
      if (node === range.endContainer) end = range.endOffset;
      if (start >= end) return;
      if (start === 0 && end === node.nodeValue.length) {
        wrapTextNode(node, id, note);
      } else {
        splitAndWrap(node, start, end, id, note);
      }
    });
  }

  function revertMark(mark) {
    var parent = mark.parentNode;
    if (!parent) return;
    if (mark.hasAttribute("data-original")) {
      var orig = mark.getAttribute("data-original");
      if (orig) parent.insertBefore(document.createTextNode(orig), mark);
      parent.removeChild(mark);
    } else {
      while (mark.firstChild) parent.insertBefore(mark.firstChild, mark);
      parent.removeChild(mark);
    }
    parent.normalize();
  }

  function revertAllMarks(root) {
    if (!root) return;
    var marks = Array.prototype.slice.call(root.querySelectorAll(".revision-mark"));
    for (var i = marks.length - 1; i >= 0; i--) revertMark(marks[i]);
  }

  function locateRange(root, rec) {
    var range = rangeFromOffsets(root, rec.start, rec.end);
    if (range && rec.text && range.toString() !== rec.text) {
      range = findTextRange(root, rec.text);
    }
    if (!range && rec.text) range = findTextRange(root, rec.text);
    return range;
  }

  function insertAppliedMark(range, rec, displayText) {
    var original = rec.text || range.toString();
    range.deleteContents();
    var mark = document.createElement("mark");
    mark.className = "revision-mark revision-applied";
    mark.dataset.revisionId = rec.id;
    mark.setAttribute("data-original", original);
    mark.dataset.action = rec.action || "edit";
    if (rec.note) mark.dataset.revisionNote = rec.note;
    if (displayText) {
      mark.textContent = displayText;
      mark.classList.add("revision-edited");
    } else {
      mark.classList.add("revision-deleted");
      mark.setAttribute("title", "Testo cancellato");
    }
    range.insertNode(mark);
  }

  function applyRecordToRoot(root, rec) {
    var action = rec.action || "segna";
    var hasReplacement = Object.prototype.hasOwnProperty.call(rec, "replacement");

    if (action === "segna" || action === "highlight" || !hasReplacement) {
      var hi = locateRange(root, rec);
      if (!hi && rec.text) hi = findTextRange(root, rec.text);
      if (hi) applyRangeHighlight(hi, rec.id, rec.note || "");
      return;
    }

    var range = locateRange(root, rec);
    if (!range && rec.replacement) {
      range = findTextRange(root, rec.replacement);
      if (range) {
        applyRangeHighlight(range, rec.id, rec.note || "");
        var existing = root.querySelector('[data-revision-id="' + rec.id + '"]');
        if (existing) {
          existing.classList.add("revision-applied", "revision-edited");
          existing.setAttribute("data-original", rec.text || "");
          existing.dataset.action = action;
        }
        return;
      }
    }
    if (!range) return;
    insertAppliedMark(range, rec, rec.replacement || "");
  }

  function applyImageFlags(episodeEl) {
    var img = episodeEl.querySelector(".episode-image");
    if (!img) return;
    img.classList.remove("revision-image-flag");
    marksForEpisode(episodeEl).forEach(function (rec) {
      if (rec.target === "image") img.classList.add("revision-image-flag");
    });
  }

  function applyStoredHighlights(episodeEl) {
    var roots = editableRoots(episodeEl);
    Object.keys(roots).forEach(function (key) {
      revertAllMarks(roots[key]);
    });

    var list = (marksForEpisode(episodeEl) || []).slice();
    var byTarget = {};
    list.forEach(function (rec) {
      var t = rec.target || "racconto";
      if (t === "image") return;
      if (!byTarget[t]) byTarget[t] = [];
      byTarget[t].push(rec);
    });

    Object.keys(byTarget).forEach(function (target) {
      var root = rootForTarget(episodeEl, target);
      if (!root) return;
      byTarget[target]
        .sort(function (a, b) {
          return (b.start || 0) - (a.start || 0);
        })
        .forEach(function (rec) {
          applyRecordToRoot(root, rec);
        });
    });

    applyImageFlags(episodeEl);
  }

  function applyAllStored() {
    document.querySelectorAll(".episode[data-episode]").forEach(applyStoredHighlights);
  }

  function getMarkRecord(episodeEl, id) {
    var list = marksForEpisode(episodeEl);
    for (var i = 0; i < list.length; i++) {
      if (list[i].id === id) return list[i];
    }
    return null;
  }

  function persistMark(episodeEl, record) {
    var data = loadAll();
    var key = episodeKey(episodeEl.dataset.episode);
    if (!data[key]) data[key] = [];
    var idx = -1;
    for (var i = 0; i < data[key].length; i++) {
      if (data[key][i].id === record.id) {
        idx = i;
        break;
      }
    }
    if (idx >= 0) data[key][idx] = record;
    else data[key].push(record);
    saveAll(data);
    updateBar();
  }

  function removeMarkRecord(episodeEl, id) {
    var data = loadAll();
    var key = episodeKey(episodeEl.dataset.episode);
    if (!data[key]) return;
    data[key] = data[key].filter(function (m) {
      return m.id !== id;
    });
    if (!data[key].length) delete data[key];
    saveAll(data);
    updateBar();
  }

  function snapshotEpisode(key) {
    var data = loadAll();
    return JSON.parse(JSON.stringify(data[key] || []));
  }

  function restoreEpisode(episodeEl, marks) {
    var data = loadAll();
    var key = episodeKey(episodeEl.dataset.episode);
    if (!marks.length) delete data[key];
    else data[key] = marks;
    saveAll(data);
    applyStoredHighlights(episodeEl);
    updateBar();
  }

  function pushUndo(episodeEl) {
    var key = episodeKey(episodeEl.dataset.episode);
    var prev = snapshotEpisode(key);
    undoStack.push({ episodeEl: episodeEl, marks: prev });
    if (undoStack.length > UNDO_LIMIT) undoStack.shift();
    updateBar();
  }

  function undoLast() {
    var item = undoStack.pop();
    if (!item) return;
    restoreEpisode(item.episodeEl, item.marks);
    closeToolbar();
    closePopovers();
    closeEditBar();
  }

  function commitRecord(episodeEl, rec) {
    pushUndo(episodeEl);
    persistMark(episodeEl, rec);
    applyStoredHighlights(episodeEl);
  }

  function currentEpisode() {
    var episodes = document.querySelectorAll(".episode[data-episode]");
    var mid = window.innerHeight * 0.35;
    for (var i = 0; i < episodes.length; i++) {
      var rect = episodes[i].getBoundingClientRect();
      if (rect.top <= mid && rect.bottom >= mid) return episodes[i];
    }
    return episodes[0] || null;
  }

  function totalMarks() {
    var data = loadAll();
    var n = 0;
    Object.keys(data).forEach(function (k) {
      n += (data[k] || []).length;
    });
    return n;
  }

  function marksForEpisode(ep) {
    if (!ep) return [];
    var data = loadAll();
    return data[episodeKey(ep.dataset.episode)] || [];
  }

  function actionLabel(action) {
    if (action === "edit") return "modifica";
    if (action === "delete") return "cancellato";
    if (action === "cut") return "tagliato";
    if (action === "paste") return "incollato";
    if (action === "image") return "illustrazione";
    return "segna";
  }

  function exportMarkdown() {
    var data = loadAll();
    var keys = Object.keys(data).sort(function (a, b) {
      return parseInt(a, 10) - parseInt(b, 10);
    });
    if (!keys.length) return "# Revisioni lettura\n\n_Nessuna evidenziazione._\n";

    var lines = ["# Revisioni lettura — " + new Date().toISOString().slice(0, 10), ""];
    keys.forEach(function (key) {
      var epEl = document.querySelector('.episode[data-episode="' + key + '"]');
      var title = epEl ? episodeTitle(epEl) : "Episodio " + key;
      lines.push("## " + title);
      lines.push("");
      (data[key] || []).forEach(function (rec, i) {
        var original = normalizeSpace(rec.text);
        var line = i + 1 + ". «" + original + "»";
        if (Object.prototype.hasOwnProperty.call(rec, "replacement")) {
          line += " → «" + normalizeSpace(rec.replacement) + "»";
        }
        line += "  [" + actionLabel(rec.action) + "]";
        lines.push(line);
        if (rec.field) lines.push("   Campo: " + rec.field);
        if (rec.note) lines.push("   Nota: " + rec.note);
        lines.push("");
      });
    });
    return lines.join("\n").trim() + "\n";
  }

  function closePopovers() {
    document.querySelectorAll(".revision-popover").forEach(function (p) {
      p.remove();
    });
  }

  function clearTempSelect() {
    document.querySelectorAll('[data-revision-id="__tmp__"]').forEach(function (m) {
      revertMark(m);
    });
    tempSelect = null;
  }

  function wrapTempSelect(snap) {
    clearTempSelect();
    if (!snap.range || snap.mark) return;
    applyRangeHighlight(snap.range, "__tmp__", "");
    var marks = snap.episodeEl.querySelectorAll('[data-revision-id="__tmp__"]');
    marks.forEach(function (m) {
      m.classList.add("revision-selecting");
    });
    tempSelect = marks[0] || null;
    var sel = window.getSelection();
    if (sel) sel.removeAllRanges();
  }

  function closeToolbar() {
    document.querySelectorAll(".revision-toolbar").forEach(function (p) {
      p.remove();
    });
    if (!editing) clearTempSelect();
  }

  function closeEditBar() {
    document.querySelectorAll(".revision-edit-bar").forEach(function (p) {
      p.remove();
    });
  }

  function closeChrome() {
    closeToolbar();
    closePopovers();
    if (!editing) closeEditBar();
  }

  function positionNearRect(el, rect) {
    var pad = 10;
    var top = rect.top - el.offsetHeight - pad;
    if (top < pad) top = Math.min(window.innerHeight - el.offsetHeight - pad, rect.bottom + pad);
    var left = rect.left + rect.width / 2 - el.offsetWidth / 2;
    left = Math.max(pad, Math.min(window.innerWidth - el.offsetWidth - pad, left));
    el.style.top = top + "px";
    el.style.left = left + "px";
  }

  function selectionRect(range) {
    var rects = range.getClientRects();
    if (rects.length) return rects[rects.length - 1];
    return range.getBoundingClientRect();
  }

  function snapshotSelection() {
    var sel = window.getSelection();
    if (!sel || sel.isCollapsed || !sel.rangeCount) return null;
    var range = sel.getRangeAt(0);
    var root = findEditableRoot(range.commonAncestorContainer);
    if (!root) return null;
    var episodeEl = findEpisode(root);
    if (!episodeEl) return null;
    var text = range.toString();
    if (normalizeSpace(text).length < 1) return null;
    var mark = range.commonAncestorContainer;
    if (mark.nodeType !== Node.ELEMENT_NODE) mark = mark.parentElement;
    mark = mark && mark.closest ? mark.closest(".revision-mark") : null;
    var info = describeTarget(root);
    var cloned = range.cloneRange();
    return {
      range: cloned,
      off: offsetsFromRange(root, cloned),
      text: text,
      root: root,
      episodeEl: episodeEl,
      rect: selectionRect(range),
      mark: mark,
      target: info.target,
      field: fieldFromRange(range) || info.field,
    };
  }

  function rangeFromSnap(snap) {
    if (snap.off) return rangeFromOffsets(snap.root, snap.off.start, snap.off.end);
    return snap.range;
  }

  function recordFromSnap(snap, extra) {
    var off = snap.off || offsetsFromRange(snap.root, snap.range);
    return Object.assign(
      {
        id: uuid(),
        start: off.start,
        end: off.end,
        text: off.text,
        note: "",
        action: "segna",
        target: snap.target,
        field: snap.field || "",
        createdAt: new Date().toISOString(),
      },
      extra
    );
  }

  function copyToClipboard(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.left = "-9999px";
      document.body.appendChild(ta);
      ta.select();
      try {
        document.execCommand("copy");
        resolve();
      } catch (err) {
        reject(err);
      }
      ta.remove();
    });
  }

  function readClipboard() {
    if (navigator.clipboard && navigator.clipboard.readText) {
      return navigator.clipboard.readText();
    }
    return Promise.reject(new Error("clipboard"));
  }

  function selectContents(el) {
    var range = document.createRange();
    range.selectNodeContents(el);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
  }

  function showEditBar(onDone, onCancel) {
    closeEditBar();
    var barEl = document.createElement("div");
    barEl.className = "revision-edit-bar";
    barEl.innerHTML =
      '<button type="button" class="revision-btn revision-btn-cancel">Annulla</button>' +
      '<span class="revision-edit-label">Modifica il testo</span>' +
      '<button type="button" class="revision-btn revision-btn-export">Fatto</button>';
    document.body.appendChild(barEl);
    barEl.querySelector(".revision-btn-cancel").addEventListener("click", function () {
      closeEditBar();
      onCancel();
    });
    barEl.querySelector(".revision-btn-export").addEventListener("click", function () {
      closeEditBar();
      onDone();
    });
  }

  function beginInlineEdit(mark, handlers) {
    editing = true;
    closeToolbar();
    closePopovers();
    mark.contentEditable = "true";
    mark.spellcheck = true;
    mark.classList.add("revision-editing");
    mark.focus();
    selectContents(mark);

    function finish(save) {
      if (!editing) return;
      editing = false;
      mark.contentEditable = "false";
      mark.classList.remove("revision-editing");
      mark.removeEventListener("keydown", onKey);
      if (save) handlers.onDone(mark.textContent);
      else handlers.onCancel();
    }

    function onKey(e) {
      if (e.key === "Enter") {
        e.preventDefault();
        document.execCommand("insertText", false, " ");
      }
      if (e.key === "Escape") {
        e.preventDefault();
        closeEditBar();
        finish(false);
      }
    }

    mark.addEventListener("keydown", onKey);
    showEditBar(
      function () {
        finish(true);
      },
      function () {
        finish(false);
      }
    );
  }

  function actCopy(snap) {
    copyToClipboard(snap.text).catch(function () {});
    closeToolbar();
  }

  function actDelete(snap, action) {
    clearTempSelect();
    if (snap.mark) {
      var rec = getMarkRecord(snap.episodeEl, snap.mark.dataset.revisionId);
      if (rec) {
        pushUndo(snap.episodeEl);
        rec.action = action;
        rec.replacement = "";
        persistMark(snap.episodeEl, rec);
        applyStoredHighlights(snap.episodeEl);
        closeToolbar();
        return;
      }
    }
    commitRecord(snap.episodeEl, recordFromSnap(snap, { action: action, replacement: "" }));
    closeToolbar();
  }

  function actCut(snap) {
    copyToClipboard(snap.text)
      .catch(function () {})
      .then(function () {
        actDelete(snap, "cut");
      });
  }

  function actPaste(snap) {
    clearTempSelect();
    readClipboard()
      .then(function (clip) {
        if (!clip) {
          window.alert("Appunti vuoti.");
          return;
        }
        if (snap.mark) {
          var rec = getMarkRecord(snap.episodeEl, snap.mark.dataset.revisionId);
          if (rec) {
            pushUndo(snap.episodeEl);
            rec.action = "paste";
            rec.replacement = clip;
            persistMark(snap.episodeEl, rec);
            applyStoredHighlights(snap.episodeEl);
            closeToolbar();
            return;
          }
        }
        commitRecord(snap.episodeEl, recordFromSnap(snap, { action: "paste", replacement: clip }));
        closeToolbar();
      })
      .catch(function () {
        var typed = window.prompt("Incolla qui il testo:", "");
        if (typed == null) return;
        commitRecord(snap.episodeEl, recordFromSnap(snap, { action: "paste", replacement: typed }));
        closeToolbar();
      });
  }

  function actSegna(snap) {
    clearTempSelect();
    if (snap.mark) {
      showNotePopover(snap.mark, snap.episodeEl);
      closeToolbar();
      return;
    }
    var rec = recordFromSnap(snap, { action: "segna" });
    commitRecord(snap.episodeEl, rec);
    closeToolbar();
    var mark = snap.episodeEl.querySelector('[data-revision-id="' + rec.id + '"]');
    if (mark) showNotePopover(mark, snap.episodeEl);
  }

  function actEdit(snap) {
    closeToolbar();
    clearTempSelect();
    if (snap.mark) {
      var rec = getMarkRecord(snap.episodeEl, snap.mark.dataset.revisionId);
      beginInlineEdit(snap.mark, {
        onDone: function (newText) {
          if (!rec) return;
          pushUndo(snap.episodeEl);
          if (!normalizeSpace(newText)) {
            rec.action = "delete";
            rec.replacement = "";
          } else if (normalizeSpace(newText) === normalizeSpace(rec.text)) {
            rec.action = "segna";
            delete rec.replacement;
          } else {
            rec.action = "edit";
            rec.replacement = newText;
          }
          persistMark(snap.episodeEl, rec);
          applyStoredHighlights(snap.episodeEl);
        },
        onCancel: function () {
          applyStoredHighlights(snap.episodeEl);
        },
      });
      return;
    }

    var off = snap.off || offsetsFromRange(snap.root, snap.range);
    var id = uuid();
    var live = rangeFromSnap(snap);
    if (!live) return;
    applyRangeHighlight(live, id, "");
    var mark = snap.episodeEl.querySelector('[data-revision-id="' + id + '"]');
    if (!mark) return;
    mark.setAttribute("data-original", off.text);
    mark.classList.add("revision-applied");

    beginInlineEdit(mark, {
      onDone: function (newText) {
        var rec = {
          id: id,
          start: off.start,
          end: off.end,
          text: off.text,
          note: "",
          target: snap.target,
          field: snap.field || "",
          createdAt: new Date().toISOString(),
        };
        if (!normalizeSpace(newText)) {
          rec.action = "delete";
          rec.replacement = "";
        } else if (normalizeSpace(newText) === normalizeSpace(off.text)) {
          rec.action = "segna";
        } else {
          rec.action = "edit";
          rec.replacement = newText;
        }
        commitRecord(snap.episodeEl, rec);
      },
      onCancel: function () {
        revertMark(mark);
      },
    });
  }

  function actRestore(snap) {
    if (!snap.mark) return;
    pushUndo(snap.episodeEl);
    removeMarkRecord(snap.episodeEl, snap.mark.dataset.revisionId);
    applyStoredHighlights(snap.episodeEl);
    closeToolbar();
  }

  function actFlagImage(episodeEl, img) {
    var existing = marksForEpisode(episodeEl).filter(function (m) {
      return m.target === "image";
    })[0];
    if (existing) {
      showImageNote(episodeEl, existing, img);
      return;
    }
    var rec = {
      id: uuid(),
      text: img.getAttribute("alt") || "Illustrazione",
      note: "",
      action: "image",
      target: "image",
      start: 0,
      end: 0,
      createdAt: new Date().toISOString(),
    };
    commitRecord(episodeEl, rec);
    showImageNote(episodeEl, rec, img);
  }

  function showImageNote(episodeEl, rec, img) {
    closeChrome();
    var pop = document.createElement("div");
    pop.className = "revision-popover";
    pop.innerHTML =
      "<label>Nota sull'illustrazione" +
      '<textarea class="revision-note-input" rows="2" placeholder="Cosa non va nel disegno?"></textarea></label>' +
      '<div class="revision-popover-actions">' +
      '<button type="button" class="revision-btn revision-btn-save-note">Salva</button>' +
      '<button type="button" class="revision-btn revision-btn-remove">Togli segno</button>' +
      "</div>";
    document.body.appendChild(pop);
    positionNearRect(pop, img.getBoundingClientRect());
    var input = pop.querySelector(".revision-note-input");
    input.value = rec.note || "";
    pop.querySelector(".revision-btn-save-note").addEventListener("click", function () {
      rec.note = input.value.trim();
      persistMark(episodeEl, rec);
      closePopovers();
    });
    pop.querySelector(".revision-btn-remove").addEventListener("click", function () {
      pushUndo(episodeEl);
      removeMarkRecord(episodeEl, rec.id);
      applyStoredHighlights(episodeEl);
      closePopovers();
    });
  }

  function showNotePopover(mark, episodeEl) {
    closePopovers();
    var id = mark.dataset.revisionId;
    var rec = getMarkRecord(episodeEl, id) || { note: mark.dataset.revisionNote || "" };
    var pop = document.createElement("div");
    pop.className = "revision-popover";
    pop.innerHTML =
      '<label>Nota <textarea class="revision-note-input" rows="2" placeholder="Perché rivedere?"></textarea></label>' +
      '<div class="revision-popover-actions">' +
      '<button type="button" class="revision-btn revision-btn-save-note">Salva nota</button>' +
      '<button type="button" class="revision-btn revision-btn-remove">Rimuovi</button>' +
      "</div>";
    document.body.appendChild(pop);
    positionNearRect(pop, mark.getBoundingClientRect());
    var input = pop.querySelector(".revision-note-input");
    input.value = rec.note || "";
    pop.querySelector(".revision-btn-save-note").addEventListener("click", function () {
      rec.note = input.value.trim();
      if (rec.note) mark.dataset.revisionNote = rec.note;
      else mark.removeAttribute("data-revision-note");
      persistMark(episodeEl, rec);
      closePopovers();
    });
    pop.querySelector(".revision-btn-remove").addEventListener("click", function () {
      pushUndo(episodeEl);
      removeMarkRecord(episodeEl, id);
      applyStoredHighlights(episodeEl);
      closePopovers();
    });
  }

  function addToolBtn(toolbar, label, className, disabled, onClick) {
    var btn = document.createElement("button");
    btn.type = "button";
    btn.textContent = label;
    if (className) btn.className = className;
    if (disabled) {
      btn.disabled = true;
      btn.title = "Presto: Gemini dal Mac";
    }
    if (onClick) btn.addEventListener("click", onClick);
    toolbar.appendChild(btn);
    return btn;
  }

  function showSelectionToolbar(snap) {
    closeToolbar();
    closePopovers();
    selSnap = snap;
    var toolbar = document.createElement("div");
    toolbar.className = "revision-toolbar";
    toolbar.setAttribute("role", "toolbar");
    toolbar.setAttribute("aria-label", "Azioni sul testo");

    if (snap.mark) {
      addToolBtn(toolbar, "Edita", "primary", false, function () {
        actEdit(snap);
      });
      addToolBtn(toolbar, "Nota", "", false, function () {
        closeToolbar();
        showNotePopover(snap.mark, snap.episodeEl);
      });
      addToolBtn(toolbar, "Copia", "", false, function () {
        actCopy({ text: snap.mark.textContent });
      });
      addToolBtn(toolbar, "Incolla", "", false, function () {
        actPaste(snap);
      });
      addToolBtn(toolbar, "Cancella", "danger", false, function () {
        actDelete(snap, "delete");
      });
      addToolBtn(toolbar, "Ripristina", "", false, function () {
        actRestore(snap);
      });
    } else {
      addToolBtn(toolbar, "Copia", "", false, function () {
        actCopy(snap);
      });
      addToolBtn(toolbar, "Taglia", "", false, function () {
        actCut(snap);
      });
      addToolBtn(toolbar, "Incolla", "", false, function () {
        actPaste(snap);
      });
      addToolBtn(toolbar, "Cancella", "danger", false, function () {
        actDelete(snap, "delete");
      });
      addToolBtn(toolbar, "Edita", "primary", false, function () {
        actEdit(snap);
      });
      addToolBtn(toolbar, "Segna", "", false, function () {
        actSegna(snap);
      });
      addToolBtn(toolbar, "Riscrivi", "", true, null);
    }

    document.body.appendChild(toolbar);
    wrapTempSelect(snap);
    var anchor = tempSelect ? tempSelect.getBoundingClientRect() : snap.rect;
    positionNearRect(toolbar, anchor);
  }

  function showExportModal(md) {
    closeChrome();
    var backdrop = document.createElement("div");
    backdrop.className = "revision-modal-backdrop";
    backdrop.innerHTML =
      '<div class="revision-modal" role="dialog">' +
      "<h3>Esporta revisioni</h3>" +
      "<p>Copia in Cursor o in un file <code>Revisioni.md</code>.</p>" +
      '<textarea class="revision-modal-code" readonly spellcheck="false"></textarea>' +
      '<div class="revision-modal-actions">' +
      '<button type="button" class="revision-btn revision-btn-copy">Copia</button>' +
      '<button type="button" class="revision-btn revision-btn-close">Chiudi</button>' +
      "</div></div>";
    document.body.appendChild(backdrop);
    var ta = backdrop.querySelector(".revision-modal-code");
    ta.value = md;
    backdrop.querySelector(".revision-btn-close").addEventListener("click", function () {
      backdrop.remove();
    });
    backdrop.addEventListener("click", function (e) {
      if (e.target === backdrop) backdrop.remove();
    });
    backdrop.querySelector(".revision-btn-copy").addEventListener("click", function () {
      ta.select();
      copyToClipboard(ta.value).then(
        function () {
          window.alert("Revisioni copiate.");
        },
        function () {
          document.execCommand("copy");
          window.alert("Revisioni copiate.");
        }
      );
    });
  }

  function clearCurrentEpisode() {
    var ep = currentEpisode();
    if (!ep) return;
    var n = marksForEpisode(ep).length;
    if (!n) return;
    if (!window.confirm("Rimuovere " + n + " revisioni da questo episodio?")) return;
    pushUndo(ep);
    var data = loadAll();
    delete data[episodeKey(ep.dataset.episode)];
    saveAll(data);
    applyStoredHighlights(ep);
    updateBar();
    closeChrome();
  }

  function buildSyncPayload() {
    var data = loadAll();
    var titles = {};
    document.querySelectorAll(".episode[data-episode]").forEach(function (ep) {
      titles[ep.dataset.episode] = episodeTitle(ep);
    });
    return {
      episodes: data,
      titles: titles,
      syncedAt: new Date().toISOString(),
      source: "elefranco-lettura",
    };
  }

  function updateSyncStatus(state, detail) {
    if (!syncStatusEl) return;
    syncStatusEl.classList.remove(
      "revision-sync-offline",
      "revision-sync-online",
      "revision-sync-busy",
      "revision-sync-ok",
      "revision-sync-error"
    );
    syncStatusEl.classList.add("revision-sync-" + state);
    syncStatusEl.textContent = detail;
  }

  function checkSyncServer() {
    if (location.protocol === "file:") {
      serverOnline = false;
      updateSyncStatus("offline", "Apri con --watch --lan");
      return;
    }
    fetch("/api/revisioni/status?t=" + Date.now())
      .then(function (r) {
        if (!r.ok) throw new Error("status");
        return r.json();
      })
      .then(function (data) {
        serverOnline = true;
        updateSyncStatus("online", "Cursor · " + (data.pendingCount || 0) + " in attesa");
        refreshExportFallback();
      })
      .catch(function () {
        serverOnline = false;
        updateSyncStatus("offline", "Solo locale");
        refreshExportFallback();
      });
  }

  function scheduleSync() {
    if (syncTimer) clearTimeout(syncTimer);
    syncTimer = setTimeout(pushSync, 400);
  }

  function pushSync() {
    syncTimer = null;
    if (location.protocol === "file:") return;

    updateSyncStatus("busy", "Sync Cursor…");

    fetch("/api/revisioni/sync", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(buildSyncPayload()),
    })
      .then(function (r) {
        if (!r.ok) throw new Error("sync failed");
        return r.json();
      })
      .then(function (data) {
        serverOnline = true;
        updateSyncStatus("ok", "In Cursor · " + (data.pendingCount || 0) + " in attesa");
        refreshExportFallback();
      })
      .catch(function () {
        serverOnline = false;
        updateSyncStatus("error", "Sync fallita");
        refreshExportFallback();
      });
  }

  function setRevisionMode(on) {
    active = on;
    document.body.classList.toggle("revision-mode", on);
    toggleBtn.setAttribute("aria-pressed", on ? "true" : "false");
    toggleBtn.textContent = on ? "Revisione ✓" : "Revisione";
    bar.hidden = !on;
    if (on) {
      checkSyncServer();
      applyAllStored();
      hint.hidden = false;
      if (hintTimer) clearTimeout(hintTimer);
      hintTimer = setTimeout(function () {
        hint.hidden = true;
      }, HINT_MS);
    } else {
      hint.hidden = true;
      closeChrome();
      closeEditBar();
      editing = false;
    }
    updateBar();
    refreshExportFallback();
  }

  function updateBar() {
    var ep = currentEpisode();
    var epCount = marksForEpisode(ep).length;
    var total = totalMarks();
    countEl.textContent = (ep ? epCount + " qui" : "0 qui") + " · " + total + " totali";
    if (undoBtn) undoBtn.disabled = !undoStack.length;
  }

  var toggleBtn = document.createElement("button");
  toggleBtn.type = "button";
  toggleBtn.id = "revision-toggle";
  toggleBtn.className = "revision-toggle";
  toggleBtn.setAttribute("aria-pressed", "false");
  toggleBtn.title = "Seleziona con la Pencil e apri il menu";
  toggleBtn.textContent = "Revisione";

  var hint = document.createElement("div");
  hint.id = "revision-hint";
  hint.className = "revision-hint";
  hint.hidden = true;
  hint.innerHTML =
    "Seleziona con la <strong>penna</strong> · tieni premuto per il menu · " +
    "dito = scorrere";

  var bar = document.createElement("div");
  bar.id = "revision-bar";
  bar.className = "revision-bar";
  bar.hidden = true;
  bar.innerHTML =
    '<span class="revision-count"></span>' +
    '<span class="revision-sync revision-sync-offline" id="revision-sync">…</span>' +
    '<button type="button" class="revision-btn revision-btn-undo" disabled>Annulla</button>' +
    '<button type="button" class="revision-btn revision-btn-export" hidden>Copia</button>' +
    '<button type="button" class="revision-btn revision-btn-clear">Pulisci episodio</button>';
  var countEl = bar.querySelector(".revision-count");
  var syncStatusEl = bar.querySelector("#revision-sync");
  var exportBtn = bar.querySelector(".revision-btn-export");
  var undoBtn = bar.querySelector(".revision-btn-undo");

  document.body.appendChild(toggleBtn);
  document.body.appendChild(hint);
  document.body.appendChild(bar);

  toggleBtn.addEventListener("click", function () {
    setRevisionMode(!active);
  });

  bar.querySelector(".revision-btn-export").addEventListener("click", function () {
    showExportModal(exportMarkdown());
  });

  function refreshExportFallback() {
    if (!exportBtn) return;
    exportBtn.hidden = serverOnline;
  }

  undoBtn.addEventListener("click", undoLast);
  bar.querySelector(".revision-btn-clear").addEventListener("click", clearCurrentEpisode);

  function isChrome(el) {
    return !!(
      el &&
      el.closest &&
      (el.closest(".revision-toolbar") ||
        el.closest(".revision-popover") ||
        el.closest(".revision-modal") ||
        el.closest(".revision-edit-bar") ||
        el.closest(".revision-bar") ||
        el.closest(".revision-toggle"))
    );
  }

  document.addEventListener("pointerdown", function (e) {
    lastPointerType = e.pointerType || "mouse";
    if (!active || editing) return;
    if (isChrome(e.target)) return;

    closeToolbar();
    closePopovers();

    if (e.target.closest(".revision-mark")) {
      longPressTarget = e.target.closest(".revision-mark");
      longPressTimer = setTimeout(function () {
        var ep = findEpisode(longPressTarget);
        if (!ep) return;
        showSelectionToolbar({
          mark: longPressTarget,
          episodeEl: ep,
          text: longPressTarget.textContent,
          rect: longPressTarget.getBoundingClientRect(),
          range: null,
          root: findEditableRoot(longPressTarget),
          target: describeTarget(findEditableRoot(longPressTarget)).target,
          field: "",
        });
        longPressTimer = null;
      }, LONG_PRESS_MS);
    }
  });

  document.addEventListener("pointerup", function (e) {
    if (longPressTimer) {
      clearTimeout(longPressTimer);
      longPressTimer = null;
    }

    if (!active || editing) return;
    if (isChrome(e.target)) return;
    if ((e.pointerType || lastPointerType) === "touch") return;

    var img = e.target.closest && e.target.closest(".episode-image");
    if (img && (e.pointerType === "pen" || e.pointerType === "mouse")) {
      var epImg = findEpisode(img);
      if (epImg && !window.getSelection().toString()) {
        actFlagImage(epImg, img);
        return;
      }
    }

    if (e.target.closest(".revision-mark") && !window.getSelection().toString()) {
      var mark = e.target.closest(".revision-mark");
      var ep = findEpisode(mark);
      if (ep) {
        showSelectionToolbar({
          mark: mark,
          episodeEl: ep,
          text: mark.textContent,
          rect: mark.getBoundingClientRect(),
          range: null,
          root: findEditableRoot(mark),
          target: describeTarget(findEditableRoot(mark)).target,
          field: "",
        });
      }
      return;
    }

    setTimeout(function () {
      if (!active || editing) return;
      var snap = snapshotSelection();
      if (snap) showSelectionToolbar(snap);
    }, 30);
  });

  document.addEventListener("pointermove", function () {
    if (longPressTimer) {
      clearTimeout(longPressTimer);
      longPressTimer = null;
    }
  });

  document.addEventListener("contextmenu", function (e) {
    if (!active) return;
    if (findEditableRoot(e.target) || (e.target.closest && e.target.closest(".episode-image"))) {
      e.preventDefault();
    }
  });

  document.addEventListener("scroll", function () {
    if (!editing) closeToolbar();
    updateBar();
  }, { passive: true });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      if (editing) return;
      closeChrome();
    }
    if ((e.metaKey || e.ctrlKey) && e.key === "z" && active && !editing) {
      e.preventDefault();
      undoLast();
    }
  });

  window.addEventListener("beforeunload", function () {
    if (syncTimer) pushSync();
  });

  checkSyncServer();
  applyAllStored();
})();
