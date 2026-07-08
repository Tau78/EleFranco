(function () {
  "use strict";

  var dataEl = document.getElementById("colora-data");
  if (!dataEl) return;

  var pages = JSON.parse(dataEl.textContent || "[]");
  if (!pages.length) return;

  var COLORS = [
    "#e74c3c",
    "#e67e22",
    "#f1c40f",
    "#2ecc71",
    "#3498db",
    "#9b59b6",
    "#e91e63",
    "#795548",
    "#2c3e50",
    "#ffffff",
  ];

  var STORAGE_PREFIX = "elefranco-colora-v1-";
  var MAX_UNDO = 30;

  var episodeSelect = document.getElementById("colora-episode");
  var prevBtn = document.getElementById("colora-prev");
  var nextBtn = document.getElementById("colora-next");
  var hintEl = document.getElementById("colora-hint");
  var bgImg = document.getElementById("colora-bg");
  var canvas = document.getElementById("colora-draw");
  var paletteEl = document.getElementById("colora-palette");
  var sizeInput = document.getElementById("colora-size");
  var undoBtn = document.getElementById("colora-undo");
  var clearBtn = document.getElementById("colora-clear");
  var saveBtn = document.getElementById("colora-save");
  var brushBtn = document.getElementById("colora-brush");
  var eraserBtn = document.getElementById("colora-eraser");
  var statusEl = document.getElementById("colora-status");

  var ctx = canvas.getContext("2d");
  var currentIndex = 0;
  var currentColor = COLORS[0];
  var brushSize = 12;
  var isEraser = false;
  var isDrawing = false;
  var undoStack = [];
  var dpr = window.devicePixelRatio || 1;

  function pageByNum(num) {
    for (var i = 0; i < pages.length; i += 1) {
      if (pages[i].num === num) return i;
    }
    return 0;
  }

  function populateSelect() {
    pages.forEach(function (page, idx) {
      var opt = document.createElement("option");
      opt.value = String(idx);
      opt.textContent = "Ep. " + page.num + " — " + page.title;
      episodeSelect.appendChild(opt);
    });
  }

  function buildPalette() {
    COLORS.forEach(function (color) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "colora-swatch";
      btn.style.background = color;
      btn.dataset.color = color;
      btn.setAttribute("aria-label", "Colore " + color);
      btn.addEventListener("click", function () {
        setColor(color);
        setEraser(false);
      });
      paletteEl.appendChild(btn);
    });
    updatePaletteActive();
  }

  function setColor(color) {
    currentColor = color;
    updatePaletteActive();
  }

  function updatePaletteActive() {
    paletteEl.querySelectorAll(".colora-swatch").forEach(function (btn) {
      btn.classList.toggle("is-active", !isEraser && btn.dataset.color === currentColor);
    });
    brushBtn.classList.toggle("is-active", !isEraser);
    eraserBtn.classList.toggle("is-active", isEraser);
  }

  function setEraser(on) {
    isEraser = on;
    updatePaletteActive();
  }

  function setStatus(msg) {
    statusEl.textContent = msg || "";
  }

  function storageKey() {
    return STORAGE_PREFIX + pages[currentIndex].num;
  }

  function resizeCanvas() {
    var rect = canvas.getBoundingClientRect();
    var w = Math.max(1, Math.round(rect.width * dpr));
    var h = Math.max(1, Math.round(rect.height * dpr));
    if (canvas.width === w && canvas.height === h) return false;
    var snapshot = canvas.width ? canvas.toDataURL("image/png") : null;
    canvas.width = w;
    canvas.height = h;
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    if (snapshot) {
      var img = new Image();
      img.onload = function () {
        ctx.drawImage(img, 0, 0, w, h);
      };
      img.src = snapshot;
    }
    return true;
  }

  function clearDrawLayer() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
  }

  function saveUndoSnapshot() {
    if (!canvas.width) return;
    undoStack.push(canvas.toDataURL("image/png"));
    if (undoStack.length > MAX_UNDO) undoStack.shift();
    undoBtn.disabled = undoStack.length === 0;
  }

  function restoreFromDataUrl(dataUrl, persist) {
    if (!dataUrl) {
      clearDrawLayer();
      undoStack = [];
      undoBtn.disabled = true;
      return;
    }
    var img = new Image();
    img.onload = function () {
      clearDrawLayer();
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      if (persist !== false) persistDrawing();
    };
    img.src = dataUrl;
  }

  function persistDrawing() {
    try {
      localStorage.setItem(storageKey(), canvas.toDataURL("image/png"));
    } catch (err) {
      setStatus("Disegno salvato in memoria (spazio pieno sul dispositivo).");
    }
  }

  function loadSavedDrawing() {
    var saved = null;
    try {
      saved = localStorage.getItem(storageKey());
    } catch (err) {
      saved = null;
    }
    undoStack = [];
    undoBtn.disabled = true;
    restoreFromDataUrl(saved, false);
  }

  function loadEpisode(index) {
    currentIndex = index;
    var page = pages[currentIndex];
    episodeSelect.value = String(currentIndex);
    hintEl.textContent = page.hint
      ? "Suggerimento: " + page.hint + "."
      : "Colora come preferisci!";
    bgImg.src = page.src;
    bgImg.alt = "Disegno episodio " + page.num;
    prevBtn.disabled = currentIndex === 0;
    nextBtn.disabled = currentIndex === pages.length - 1;

    var params = new URLSearchParams(window.location.search);
    params.set("ep", String(page.num));
    history.replaceState(null, "", "?" + params.toString());
  }

  function pointerPos(evt) {
    var rect = canvas.getBoundingClientRect();
    var clientX = evt.clientX;
    var clientY = evt.clientY;
    if (evt.touches && evt.touches[0]) {
      clientX = evt.touches[0].clientX;
      clientY = evt.touches[0].clientY;
    }
    return {
      x: (clientX - rect.left) * dpr,
      y: (clientY - rect.top) * dpr,
    };
  }

  function strokeStyle() {
    if (isEraser) {
      ctx.globalCompositeOperation = "destination-out";
      return "rgba(0,0,0,1)";
    }
    ctx.globalCompositeOperation = "source-over";
    return currentColor;
  }

  function startDraw(evt) {
    evt.preventDefault();
    isDrawing = true;
    saveUndoSnapshot();
    var p = pointerPos(evt);
    ctx.beginPath();
    ctx.moveTo(p.x, p.y);
    ctx.strokeStyle = strokeStyle();
    ctx.lineWidth = brushSize * dpr;
    ctx.lineTo(p.x + 0.01, p.y + 0.01);
    ctx.stroke();
  }

  function moveDraw(evt) {
    if (!isDrawing) return;
    evt.preventDefault();
    var p = pointerPos(evt);
    ctx.strokeStyle = strokeStyle();
    ctx.lineWidth = brushSize * dpr;
    ctx.lineTo(p.x, p.y);
    ctx.stroke();
  }

  function endDraw(evt) {
    if (!isDrawing) return;
    if (evt) evt.preventDefault();
    isDrawing = false;
    ctx.closePath();
    ctx.globalCompositeOperation = "source-over";
    persistDrawing();
  }

  function exportComposite() {
    var out = document.createElement("canvas");
    out.width = canvas.width;
    out.height = canvas.height;
    var outCtx = out.getContext("2d");
    outCtx.fillStyle = "#ffffff";
    outCtx.fillRect(0, 0, out.width, out.height);
    if (bgImg.complete && bgImg.naturalWidth) {
      var scale = Math.min(out.width / bgImg.naturalWidth, out.height / bgImg.naturalHeight);
      var dw = bgImg.naturalWidth * scale;
      var dh = bgImg.naturalHeight * scale;
      var dx = (out.width - dw) / 2;
      var dy = (out.height - dh) / 2;
      outCtx.drawImage(bgImg, dx, dy, dw, dh);
    }
    outCtx.drawImage(canvas, 0, 0);
    return out;
  }

  function downloadDrawing() {
    var page = pages[currentIndex];
    var out = exportComposite();
    out.toBlob(function (blob) {
      if (!blob) {
        setStatus("Impossibile salvare l'immagine.");
        return;
      }
      var url = URL.createObjectURL(blob);
      var a = document.createElement("a");
      a.href = url;
      a.download = "EleFranco-colora-" + String(page.num).padStart(2, "0") + ".png";
      document.body.appendChild(a);
      a.click();
      a.remove();
      setTimeout(function () {
        URL.revokeObjectURL(url);
      }, 2000);
      setStatus("Salvato! Su iPad: Condividi → Salva immagine.");
    }, "image/png");
  }

  bgImg.addEventListener("load", function () {
    resizeCanvas();
    loadSavedDrawing();
  });

  canvas.addEventListener("mousedown", startDraw);
  canvas.addEventListener("mousemove", moveDraw);
  window.addEventListener("mouseup", endDraw);
  canvas.addEventListener("touchstart", startDraw, { passive: false });
  canvas.addEventListener("touchmove", moveDraw, { passive: false });
  canvas.addEventListener("touchend", endDraw, { passive: false });
  canvas.addEventListener("touchcancel", endDraw, { passive: false });

  window.addEventListener("resize", function () {
    var saved = null;
    try {
      saved = localStorage.getItem(storageKey());
    } catch (err) {
      saved = null;
    }
    resizeCanvas();
    restoreFromDataUrl(saved, false);
  });

  episodeSelect.addEventListener("change", function () {
    loadEpisode(Number(episodeSelect.value));
    if (bgImg.complete) loadSavedDrawing();
  });

  prevBtn.addEventListener("click", function () {
    if (currentIndex > 0) {
      loadEpisode(currentIndex - 1);
      if (bgImg.complete) loadSavedDrawing();
    }
  });

  nextBtn.addEventListener("click", function () {
    if (currentIndex < pages.length - 1) {
      loadEpisode(currentIndex + 1);
      if (bgImg.complete) loadSavedDrawing();
    }
  });

  sizeInput.addEventListener("input", function () {
    brushSize = Number(sizeInput.value);
  });

  brushBtn.addEventListener("click", function () {
    setEraser(false);
  });

  eraserBtn.addEventListener("click", function () {
    setEraser(true);
  });

  undoBtn.addEventListener("click", function () {
    var prev = undoStack.pop();
    undoBtn.disabled = undoStack.length === 0;
    restoreFromDataUrl(prev || null);
    persistDrawing();
  });

  clearBtn.addEventListener("click", function () {
    if (!window.confirm("Cancellare tutti i colori di questo disegno?")) return;
    saveUndoSnapshot();
    clearDrawLayer();
    persistDrawing();
  });

  saveBtn.addEventListener("click", downloadDrawing);

  populateSelect();
  buildPalette();

  var startEp = Number(new URLSearchParams(window.location.search).get("ep"));
  if (startEp) currentIndex = pageByNum(startEp);
  loadEpisode(currentIndex);
})();
