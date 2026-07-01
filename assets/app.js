// Datos Abiertos MX — Explorador
// Carga assets/manifest.json, renderiza sidebar de sectores + grid de cards,
// y al click carga la ficha .md correspondiente vía fetch + marked.

(function () {
  'use strict';

  const state = {
    manifest: null,
    activeSector: 'all',
    query: '',
  };

  const el = {
    sectorList: document.getElementById('sector-list'),
    grid: document.getElementById('grid'),
    emptyState: document.getElementById('empty-state'),
    contentTitle: document.getElementById('content-title'),
    contentCount: document.getElementById('content-count'),
    statTotal: document.getElementById('stat-total'),
    searchInput: document.getElementById('search-input'),
    overlay: document.getElementById('overlay'),
    detailPanel: document.getElementById('detail-panel'),
    detailContent: document.getElementById('detail-content'),
    detailClose: document.getElementById('detail-close'),
  };

  async function init() {
    try {
      const res = await fetch('assets/manifest.json', { cache: 'no-store' });
      state.manifest = await res.json();
    } catch (e) {
      el.grid.innerHTML = '<p style="color:#f87171">No se pudo cargar manifest.json — corre build_manifest.py</p>';
      return;
    }
    el.statTotal.textContent = `${state.manifest.totalSources} fuentes · ${state.manifest.totalSectors} sectores`;
    renderSectorList();
    renderGrid();
    bindEvents();
  }

  function renderSectorList() {
    const { sectors, sources } = state.manifest;
    const counts = {};
    sources.forEach((s) => { counts[s.sector] = (counts[s.sector] || 0) + 1; });

    const allItem = sectorItemHtml('all', 'Todas', sources.length, '#f5c344', false);
    const items = Object.entries(sectors).map(([key, meta]) => {
      const count = counts[key] || 0;
      return sectorItemHtml(key, meta.label, count, meta.color, count === 0);
    });

    el.sectorList.innerHTML = allItem + items.join('');
    markActiveSector();

    el.sectorList.querySelectorAll('.sector-item:not(.empty)').forEach((node) => {
      node.addEventListener('click', () => {
        state.activeSector = node.dataset.sector;
        renderSectorList();
        renderGrid();
      });
    });
  }

  function sectorItemHtml(key, label, count, color, isEmpty) {
    return `
      <div class="sector-item${isEmpty ? ' empty' : ''}" data-sector="${key}" style="--sector-color:${color}">
        <span class="name"><span class="sw"></span>${label}</span>
        <span class="cnt">${count}</span>
      </div>`;
  }

  function markActiveSector() {
    el.sectorList.querySelectorAll('.sector-item').forEach((node) => {
      node.classList.toggle('active', node.dataset.sector === state.activeSector);
    });
  }

  function getFilteredSources() {
    const { sources } = state.manifest;
    const q = state.query.trim().toLowerCase();
    return sources.filter((s) => {
      if (state.activeSector !== 'all' && s.sector !== state.activeSector) return false;
      if (!q) return true;
      const hay = `${s.title} ${s.institucion} ${s.descripcion} ${s.sectorLabel}`.toLowerCase();
      return hay.includes(q);
    });
  }

  function renderGrid() {
    const filtered = getFilteredSources();
    const sectorMeta = state.manifest.sectors;
    const activeLabel = state.activeSector === 'all'
      ? 'Todas las fuentes'
      : (sectorMeta[state.activeSector]?.label || state.activeSector);

    el.contentTitle.textContent = activeLabel;
    el.contentCount.textContent = `${filtered.length} ficha${filtered.length === 1 ? '' : 's'}`;

    if (filtered.length === 0) {
      el.grid.innerHTML = '';
      el.emptyState.hidden = false;
      return;
    }
    el.emptyState.hidden = true;

    el.grid.innerHTML = filtered.map(cardHtml).join('');

    el.grid.querySelectorAll('.card').forEach((node) => {
      node.addEventListener('click', () => openDetail(node.dataset.id));
    });
  }

  function cardHtml(s) {
    const color = state.manifest.sectors[s.sector]?.color || '#f5c344';
    return `
      <article class="card" data-id="${escapeAttr(s.id)}" style="--sector-color:${color}">
        <div class="card-top">
          <span class="card-sector-tag">${escapeHtml(s.sectorLabel)}</span>
          <span class="card-format">${escapeHtml(shorten(s.formato, 22))}</span>
        </div>
        <h3>${escapeHtml(s.title)}</h3>
        <div class="card-inst">${escapeHtml(s.institucion)}</div>
        <p class="card-desc">${escapeHtml(s.descripcion)}</p>
        <div class="card-meta-row">
          <span>🗓 ${escapeHtml(shorten(s.periodicidad, 18))}</span>
          <span>📍 ${escapeHtml(shorten(s.coberturaGeo, 16))}</span>
        </div>
      </article>`;
  }

  async function openDetail(id) {
    const source = state.manifest.sources.find((s) => s.id === id);
    if (!source) return;

    el.overlay.hidden = false;
    el.detailPanel.hidden = false;
    el.detailContent.innerHTML = '<div class="loader">Cargando ficha…</div>';
    document.body.style.overflow = 'hidden';

    try {
      const res = await fetch(source.path, { cache: 'no-store' });
      const md = await res.text();
      const html = window.marked ? window.marked.parse(md) : `<pre>${escapeHtml(md)}</pre>`;
      el.detailContent.innerHTML = html;
    } catch (e) {
      el.detailContent.innerHTML = `<p style="color:#f87171">No se pudo cargar la ficha: ${escapeHtml(source.path)}</p>`;
    }
  }

  function closeDetail() {
    el.overlay.hidden = true;
    el.detailPanel.hidden = true;
    document.body.style.overflow = '';
  }

  function bindEvents() {
    el.searchInput.addEventListener('input', (e) => {
      state.query = e.target.value;
      renderGrid();
    });
    el.detailClose.addEventListener('click', closeDetail);
    el.overlay.addEventListener('click', closeDetail);
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeDetail();
    });
  }

  function shorten(str, max) {
    if (!str) return '—';
    return str.length > max ? str.slice(0, max - 1) + '…' : str;
  }

  function escapeHtml(str) {
    return String(str ?? '').replace(/[&<>"']/g, (c) => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
    }[c]));
  }
  function escapeAttr(str) { return escapeHtml(str); }

  init();
})();
