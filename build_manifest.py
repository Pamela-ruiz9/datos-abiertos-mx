#!/usr/bin/env python3
"""Genera assets/manifest.json a partir de las fichas en catalogo/**/*.md"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
CATALOGO = ROOT / "catalogo"

SECTOR_META = {
    "economia": {"label": "Economía", "icon": "trending-up", "color": "#f59e0b"},
    "finanzas": {"label": "Finanzas", "icon": "landmark", "color": "#22d3ee"},
    "salud": {"label": "Salud", "icon": "heart-pulse", "color": "#f472b6"},
    "educacion": {"label": "Educación", "icon": "graduation-cap", "color": "#a78bfa"},
    "medio-ambiente": {"label": "Medio Ambiente", "icon": "leaf", "color": "#34d399"},
    "seguridad": {"label": "Seguridad", "icon": "shield-alert", "color": "#f87171"},
    "demografia": {"label": "Demografía", "icon": "users", "color": "#60a5fa"},
    "ciencia-tecnologia": {"label": "Ciencia y Tecnología", "icon": "flask-conical", "color": "#fbbf24"},
}

def parse_metadata_table(text):
    """Extrae la tabla de metadata: | **Campo** | Valor |"""
    meta = {}
    m = re.search(r"## Metadata\s*\n\n(.*?)\n\n", text, re.S)
    if not m:
        return meta
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 2:
            continue
        key = re.sub(r"\*\*", "", cells[0]).strip()
        val = cells[1].strip()
        if key in ("Campo", "-------") or set(key) == {"-"}:
            continue
        meta[key] = val
    return meta

def get_title(text):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else "Sin título"

def get_description(text):
    m = re.search(r"## Descripción\s*\n\n(.+?)\n\n", text, re.S)
    if m:
        return m.group(1).strip().split("\n")[0]
    return ""

def main():
    sources = []
    for sector_dir in sorted(CATALOGO.iterdir()):
        if not sector_dir.is_dir():
            continue
        sector_key = sector_dir.name
        for md_file in sorted(sector_dir.glob("*.md")):
            text = md_file.read_text(encoding="utf-8")
            meta = parse_metadata_table(text)
            sources.append({
                "id": f"{sector_key}/{md_file.stem}",
                "title": get_title(text),
                "sector": sector_key,
                "sectorLabel": SECTOR_META.get(sector_key, {}).get("label", sector_key),
                "institucion": meta.get("Institución", ""),
                "periodicidad": meta.get("Periodicidad", ""),
                "formato": meta.get("Formato", ""),
                "licencia": meta.get("Licencia", ""),
                "coberturaGeo": meta.get("Cobertura geográfica", ""),
                "coberturaTemporal": meta.get("Cobertura temporal", ""),
                "descripcion": get_description(text),
                "path": str(md_file.relative_to(ROOT)),
            })

    manifest = {
        "generatedFrom": "catalogo/",
        "sectors": SECTOR_META,
        "sources": sources,
        "totalSources": len(sources),
        "totalSectors": len(SECTOR_META),
    }

    out_dir = ROOT / "assets"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "manifest.json"
    out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ {len(sources)} fuentes indexadas en {out_path}")

if __name__ == "__main__":
    main()
