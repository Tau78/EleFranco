/**
 * Console Papà v2 — editor visuale del libro EleFranco.
 * Testo editabile ovunque, blocchi trascinabili, toolbar immagini.
 * Persistenza in localStorage (sovrascritta da aggiorna_libro.py).
 */
(function () {
  "use strict";

  var EP_PREFIX = "elefranco-console-papa-ep-";
  var SEC_PREFIX = "elefranco-console-papa-section-";
  var NAV_PREFIX = "elefranco-console-papa-nav-";

  var toggle = document.getElementById("console-papa-toggle");
  if (!toggle) return;

  var active = false;
  var modalBackdrop = null;
  var imagePanel = null;
  var selectedImage = null;
  var dragBlock = null;

  function storageKeyEp(num) {
    return EP_PREFIX + num;
  }

  function storageKeySection(id) {
    return SEC_PREFIX + id;
  }

  function storageKeyNav() {
    return NAV_PREFIX + location.pathname.replace(/\W/g, "_");
  }

  function editableTextNodes(root) {
    return root.querySelectorAll(".console-editable");
  }

  function serializeEpisode(episode) {
    var layout = episode.querySelector(".episode-layout");
    return {
      layoutHtml: layout ? layout.innerHTML : "",
      savedAt: new Date().toISOString(),
    };
  }

  function serializeSection(section) {
    var clone = section.cloneNode(true);
    clone.querySelectorAll(".console-section-bar").forEach(function (n) {
      n.remove();
    });
    clone.querySelectorAll(".console-drag-handle").forEach(function (n) {
      n.remove();
    });
    clone.querySelectorAll("[contenteditable]").forEach(function (n) {
      n.removeAttribute("contenteditable");
      n.removeAttribute("spellcheck");
    });
    clone.querySelectorAll(".console-block-selected").forEach(function (n) {
      n.classList.remove("console-block-selected");
    });
    return {
      sectionHtml: clone.innerHTML,
      savedAt: new Date().toISOString(),
    };
  }

  function applyEpisodePayload(episode, payload) {
    if (!payload || !payload.layoutHtml) return;
    var layout = episode.querySelector(".episode-layout");
    if (layout) layout.innerHTML = payload.layoutHtml;
  }

  function applySectionPayload(section, payload) {
    if (!payload || !payload.sectionHtml) return;
    var bar = section.querySelector(".console-section-bar");
    section.innerHTML = payload.sectionHtml;
    if (bar) section.insertBefore(bar, section.firstChild);
  }

  function loadSavedEdits() {
    document.querySelectorAll(".episode[data-episode]").forEach(function (episode) {
      var num = episode.getAttribute("data-episode");
      var raw = localStorage.getItem(storageKeyEp(num));
      if (!raw) return;
      try {
        applyEpisodePayload(episode, JSON.parse(raw));
      } catch (e) {
        console.warn("Console Papà: dati corrotti episodio", num);
      }
    });

    document.querySelectorAll(".console-section[data-console-section]").forEach(function (section) {
      var id = section.getAttribute("data-console-section");
      if (id === "chapter-nav") return;
      var raw = localStorage.getItem(storageKeySection(id));
      if (!raw) return;
      try {
        applySectionPayload(section, JSON.parse(raw));
      } catch (e) {
        console.warn("Console Papà: dati corrotti sezione", id);
      }
    });

    var nav = document.querySelector('.chapter-nav[data-console-section="chapter-nav"]');
    if (nav) {
      var navRaw = localStorage.getItem(storageKeyNav());
      if (navRaw) {
        try {
          nav.outerHTML = JSON.parse(navRaw).navHtml;
        } catch (e) {
          console.warn("Console Papà: nav corrotta");
        }
      }
    }
  }

  function setContentEditable(nodes, on) {
    nodes.forEach(function (node) {
      if (on) {
        node.setAttribute("contenteditable", "true");
        node.setAttribute("spellcheck", "true");
      } else {
        node.removeAttribute("contenteditable");
        node.removeAttribute("spellcheck");
      }
    });
  }

  function injectDragHandles(layout) {
    layout.querySelectorAll(".console-block").forEach(function (block) {
      if (block.querySelector(".console-drag-handle")) return;
      var handle = document.createElement("button");
      handle.type = "button";
      handle.className = "console-drag-handle";
      handle.setAttribute("aria-label", "Trascina per spostare blocco");
      handle.textContent = "⋮⋮";
      block.insertBefore(handle, block.firstChild);
    });
  }

  function removeDragHandles(root) {
    root.querySelectorAll(".console-drag-handle").forEach(function (h) {
      h.remove();
    });
  }

  function setupBlockDrag(layout) {
    injectDragHandles(layout);

    layout.querySelectorAll(".console-block").forEach(function (block) {
      block.setAttribute("draggable", "true");
    });

    if (layout.dataset.consoleDragReady) return;
    layout.dataset.consoleDragReady = "1";

    layout.addEventListener("dragstart", function (e) {
      var block = e.target.closest(".console-block");
      if (!block || !layout.contains(block)) return;
      if (e.target.closest(".console-editable") && !e.target.closest(".console-drag-handle")) {
        e.preventDefault();
        return;
      }
      dragBlock = block;
      block.classList.add("console-block-dragging");
      e.dataTransfer.effectAllowed = "move";
      e.dataTransfer.setData("text/plain", block.getAttribute("data-block") || "block");
    });

    layout.addEventListener("dragend", function () {
      if (dragBlock) dragBlock.classList.remove("console-block-dragging");
      dragBlock = null;
      layout.querySelectorAll(".console-block-drop-target").forEach(function (n) {
        n.classList.remove("console-block-drop-target");
      });
    });

    layout.addEventListener("dragover", function (e) {
      if (!dragBlock) return;
      e.preventDefault();
      var target = e.target.closest(".console-block");
      if (!target || target === dragBlock) return;
      layout.querySelectorAll(".console-block-drop-target").forEach(function (n) {
        n.classList.remove("console-block-drop-target");
      });
      target.classList.add("console-block-drop-target");
    });

    layout.addEventListener("drop", function (e) {
      e.preventDefault();
      if (!dragBlock) return;
      var target = e.target.closest(".console-block");
      if (!target || target === dragBlock) return;
      var rect = target.getBoundingClientRect();
      var before = e.clientY < rect.top + rect.height / 2;
      if (before) {
        layout.insertBefore(dragBlock, target);
      } else {
        layout.insertBefore(dragBlock, target.nextSibling);
      }
      target.classList.remove("console-block-drop-target");
    });
  }

  function moveBlock(block, direction) {
    var layout = block.closest(".episode-layout");
    if (!layout) return;
    if (direction === "up" && block.previousElementSibling) {
      layout.insertBefore(block, block.previousElementSibling);
    }
    if (direction === "down" && block.nextElementSibling) {
      layout.insertBefore(block.nextElementSibling, block);
    }
  }

  function closeImagePanel() {
    if (imagePanel) {
      imagePanel.remove();
      imagePanel = null;
    }
    if (selectedImage) {
      selectedImage.classList.remove("console-image-selected");
      selectedImage = null;
    }
  }

  function applyImageWidth(img, pct) {
    img.style.maxWidth = pct + "%";
    img.style.width = pct === 100 ? "100%" : pct + "%";
    img.setAttribute("data-console-width", String(pct));
  }

  function applyImageAlign(img, align) {
    img.classList.remove(
      "console-img-align-left",
      "console-img-align-center",
      "console-img-align-right",
      "console-img-float-left",
      "console-img-float-right"
    );
    if (align) img.classList.add("console-img-align-" + align);
    img.setAttribute("data-console-align", align || "center");
  }

  function showImagePanel(img) {
    closeImagePanel();
    selectedImage = img;
    img.classList.add("console-image-selected");

    var block = img.closest(".console-block");
    var isImg = img.tagName === "IMG";

    imagePanel = document.createElement("div");
    imagePanel.className = "console-image-panel";
    imagePanel.innerHTML =
      '<div class="console-image-panel-inner">' +
      "<strong>Immagine</strong>" +
      (isImg
        ? '<label>Alt <input type="text" class="console-img-alt" value="' +
          escapeAttr(img.getAttribute("alt") || "") +
          '"></label>' +
          '<label>Percorso <input type="text" class="console-img-src" value="' +
          escapeAttr(img.getAttribute("src") || "") +
          '"></label>'
        : "") +
      '<div class="console-image-panel-row">' +
      '<span>Larghezza</span>' +
      '<button type="button" data-width="40">40%</button>' +
      '<button type="button" data-width="60">60%</button>' +
      '<button type="button" data-width="80">80%</button>' +
      '<button type="button" data-width="100">100%</button>' +
      "</div>" +
      '<div class="console-image-panel-row">' +
      '<span>Allineamento</span>' +
      '<button type="button" data-align="left">Sinistra</button>' +
      '<button type="button" data-align="center">Centro</button>' +
      '<button type="button" data-align="right">Destra</button>' +
      '<button type="button" data-align="float-left">Flottante sx</button>' +
      '<button type="button" data-align="float-right">Flottante dx</button>' +
      "</div>" +
      (block
        ? '<div class="console-image-panel-row">' +
          '<span>Posizione blocco</span>' +
          '<button type="button" data-move="up">↑ Su</button>' +
          '<button type="button" data-move="down">↓ Giù</button>' +
          "</div>"
        : "") +
      '<button type="button" class="console-image-panel-close">Chiudi</button>' +
      "</div>";

    document.body.appendChild(imagePanel);

    if (isImg) {
      var altInput = imagePanel.querySelector(".console-img-alt");
      var srcInput = imagePanel.querySelector(".console-img-src");
      altInput.addEventListener("input", function () {
        img.setAttribute("alt", altInput.value);
      });
      srcInput.addEventListener("change", function () {
        img.setAttribute("src", srcInput.value.trim());
      });
    }

    imagePanel.querySelectorAll("[data-width]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        applyImageWidth(img, parseInt(btn.getAttribute("data-width"), 10));
      });
    });

    imagePanel.querySelectorAll("[data-align]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        applyImageAlign(img, btn.getAttribute("data-align"));
      });
    });

    imagePanel.querySelectorAll("[data-move]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (block) moveBlock(block, btn.getAttribute("data-move"));
      });
    });

    imagePanel.querySelector(".console-image-panel-close").addEventListener("click", closeImagePanel);
  }

  function escapeAttr(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/"/g, "&quot;")
      .replace(/</g, "&lt;");
  }

  function enableEditorMode(on) {
    active = on;
    document.body.classList.toggle("console-papa-active", on);
    toggle.setAttribute("aria-pressed", on ? "true" : "false");
    toggle.textContent = on ? "Console Papà ✓" : "Console Papà";

    if (!on) closeImagePanel();

    document.querySelectorAll(".episode[data-episode]").forEach(function (episode) {
      var layout = episode.querySelector(".episode-layout");
      var bar = episode.querySelector(".episode-console-bar");
      if (bar) bar.hidden = !on;
      setContentEditable(editableTextNodes(episode), on);
      if (layout) {
        if (on) setupBlockDrag(layout);
        else removeDragHandles(layout);
      }
    });

    document.querySelectorAll(".console-section[data-console-section]").forEach(function (section) {
      var bar = section.querySelector(".console-section-bar");
      if (bar) bar.hidden = !on;
      setContentEditable(editableTextNodes(section), on);
    });

    var hint = document.getElementById("console-papa-hint");
    if (on && !hint) {
      hint = document.createElement("div");
      hint.id = "console-papa-hint";
      hint.className = "console-papa-hint";
      hint.innerHTML =
        "Clicca il testo per modificarlo · trascina <strong>⋮⋮</strong> per spostare blocchi · clicca un'immagine per opzioni · Salva per tenere le modifiche";
      document.body.appendChild(hint);
    } else if (!on && hint) {
      hint.remove();
    }
  }

  function cleanExportClone(root) {
    var clone = root.cloneNode(true);
    clone.querySelectorAll(".episode-console-bar, .console-section-bar").forEach(function (n) {
      n.remove();
    });
    clone.querySelectorAll(".console-drag-handle").forEach(function (n) {
      n.remove();
    });
    clone.querySelectorAll("[contenteditable]").forEach(function (n) {
      n.removeAttribute("contenteditable");
      n.removeAttribute("spellcheck");
    });
    clone.querySelectorAll(".console-block-dragging, .console-block-drop-target, .console-image-selected").forEach(
      function (n) {
        n.classList.remove("console-block-dragging", "console-block-drop-target", "console-image-selected");
      }
    );
    clone.querySelectorAll(".console-block").forEach(function (block) {
      block.removeAttribute("draggable");
    });
    return clone;
  }

  function chapterHtmlExport(episode) {
    return cleanExportClone(episode).outerHTML;
  }

  function closeModal() {
    if (modalBackdrop) {
      modalBackdrop.remove();
      modalBackdrop = null;
    }
  }

  function showExportModal(title, html, note) {
    closeModal();
    modalBackdrop = document.createElement("div");
    modalBackdrop.className = "console-papa-modal-backdrop";
    modalBackdrop.innerHTML =
      '<div class="console-papa-modal" role="dialog" aria-labelledby="console-papa-modal-title">' +
      '<h3 id="console-papa-modal-title">' +
      title +
      "</h3>" +
      '<p class="console-papa-modal-note">' +
      (note ||
        "Salvato in localStorage. Al refresh resta. Rigenerando da Python si sovrascrive il file HTML.") +
      "</p>" +
      '<textarea class="console-papa-modal-code" readonly spellcheck="false"></textarea>' +
      '<div class="console-papa-modal-actions">' +
      '<button type="button" class="console-papa-btn console-papa-btn-copy">Copia HTML</button>' +
      '<button type="button" class="console-papa-btn console-papa-btn-close">Chiudi</button>' +
      "</div></div>";

    document.body.appendChild(modalBackdrop);
    var textarea = modalBackdrop.querySelector(".console-papa-modal-code");
    textarea.value = html;

    modalBackdrop.querySelector(".console-papa-btn-close").addEventListener("click", closeModal);
    modalBackdrop.addEventListener("click", function (e) {
      if (e.target === modalBackdrop) closeModal();
    });
    modalBackdrop.querySelector(".console-papa-btn-copy").addEventListener("click", function () {
      textarea.select();
      navigator.clipboard.writeText(textarea.value).then(
        function () {
          alert("HTML copiato negli appunti.");
        },
        function () {
          document.execCommand("copy");
          alert("HTML copiato.");
        }
      );
    });
  }

  function saveEpisode(episode) {
    var num = episode.getAttribute("data-episode");
    if (!num) return;
    localStorage.setItem(storageKeyEp(num), JSON.stringify(serializeEpisode(episode)));
    showExportModal("Capitolo " + num + " — salvato", chapterHtmlExport(episode));
  }

  function saveSection(section) {
    var id = section.getAttribute("data-console-section");
    if (!id) return;
    if (id === "chapter-nav") {
      localStorage.setItem(
        storageKeyNav(),
        JSON.stringify({ navHtml: section.outerHTML, savedAt: new Date().toISOString() })
      );
      showExportModal("Navigazione — salvata", section.outerHTML);
      return;
    }
    localStorage.setItem(storageKeySection(id), JSON.stringify(serializeSection(section)));
    showExportModal("Sezione " + id + " — salvata", cleanExportClone(section).outerHTML);
  }

  function resetEpisode(episode) {
    var num = episode.getAttribute("data-episode");
    if (!num) return;
    if (!confirm("Ripristinare il capitolo " + num + " alla versione generata da Python?")) return;
    localStorage.removeItem(storageKeyEp(num));
    location.reload();
  }

  function resetSection(section) {
    var id = section.getAttribute("data-console-section");
    if (!id) return;
    if (!confirm("Ripristinare la sezione «" + id + "» alla versione generata da Python?")) return;
    if (id === "chapter-nav") {
      localStorage.removeItem(storageKeyNav());
    } else {
      localStorage.removeItem(storageKeySection(id));
    }
    location.reload();
  }

  toggle.addEventListener("click", function () {
    enableEditorMode(!active);
  });

  document.addEventListener("click", function (e) {
    if (e.target.closest(".btn-save-chapter")) {
      var ep = e.target.closest(".episode");
      if (ep) saveEpisode(ep);
      return;
    }
    if (e.target.closest(".btn-reset-chapter")) {
      var epR = e.target.closest(".episode");
      if (epR) resetEpisode(epR);
      return;
    }
    if (e.target.closest(".btn-save-section")) {
      var sec = e.target.closest(".console-section");
      if (sec) saveSection(sec);
      return;
    }
    if (e.target.closest(".btn-reset-section")) {
      var secR = e.target.closest(".console-section");
      if (secR) resetSection(secR);
      return;
    }

    if (active && e.target.closest(".console-editable-image")) {
      e.preventDefault();
      showImagePanel(e.target.closest(".console-editable-image"));
      return;
    }

    if (active && imagePanel && !e.target.closest(".console-image-panel")) {
      if (!e.target.closest(".console-editable-image")) closeImagePanel();
    }
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      closeModal();
      closeImagePanel();
    }
  });

  loadSavedEdits();
})();
