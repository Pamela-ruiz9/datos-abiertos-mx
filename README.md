<div class="dam-hero" markdown>
<span class="dam-emoji">📚</span>

# Diccionario de Datos Abiertos — México

Un mapa de qué existe, dónde está, qué contiene y cómo usarlo.

<div class="dam-stats" markdown>
<span class="dam-pill">15 fuentes documentadas</span>
<span class="dam-pill">8 sectores</span>
<span class="dam-pill">actualizado 2026-06</span>
</div>
</div>

Repositorio creado y mantenido por [Pame Ruiz](https://github.com/Pamela-ruiz9).

---

## ¿Qué es esto?

Un directorio estructurado de fuentes de **datos abiertos públicos de México**: portales gubernamentales, series estadísticas, APIs, catálogos sectoriales y bases de datos temáticas.

Para cada fuente documentamos:
- Qué contiene
- Quién la publica
- Qué formato tiene
- Cómo acceder (URL, API, descarga)
- Periodicidad de actualización
- Notas de calidad / limitaciones

---

## Explora por sector

<div class="dam-grid" markdown>
<a class="dam-card" href="catalogo/finanzas/banxico-sie.md"><span class="dam-card-emoji">🏦</span><strong>Finanzas</strong><span class="dam-card-count">Banxico, CNBV</span></a>
<a class="dam-card" href="catalogo/economia/enoe-empleo.md"><span class="dam-card-emoji">📊</span><strong>Economía</strong><span class="dam-card-count">ENOE, SAT, SHCP</span></a>
<a class="dam-card" href="catalogo/salud/ssa-dge-datos-epidemiologicos.md"><span class="dam-card-emoji">🏥</span><strong>Salud</strong><span class="dam-card-count">SSA/DGE, IMSS</span></a>
<a class="dam-card" href="catalogo/educacion/sep-estadisticas.md"><span class="dam-card-emoji">🎓</span><strong>Educación</strong><span class="dam-card-count">SEP, MEJOREDU</span></a>
<a class="dam-card" href="catalogo/medio-ambiente/sinaica-calidad-aire.md"><span class="dam-card-emoji">🌳</span><strong>Medio Ambiente</strong><span class="dam-card-count">SINAICA, SEMARNAT</span></a>
<a class="dam-card" href="catalogo/seguridad/sesnsp-incidencia-delictiva.md"><span class="dam-card-emoji">🔒</span><strong>Seguridad</strong><span class="dam-card-count">SESNSP</span></a>
<a class="dam-card" href="catalogo/demografia/inegi.md"><span class="dam-card-emoji">👥</span><strong>Demografía</strong><span class="dam-card-count">INEGI, CONAPO</span></a>
<a class="dam-card" href="catalogo/ciencia-tecnologia/conacyt-indicadores-id.md"><span class="dam-card-emoji">💻</span><strong>Ciencia y Tecnología</strong><span class="dam-card-count">CONACYT/SECITI</span></a>
</div>

---

## Estructura del repositorio

```
datos-abiertos-mx/
├── README.md                  ← este archivo
├── CONTRIBUTING.md            ← cómo colaborar
├── catalogo/                  ← fichas por fuente (Markdown)
│   ├── economia/
│   ├── finanzas/
│   ├── salud/
│   ├── educacion/
│   ├── medio-ambiente/
│   ├── seguridad/
│   ├── demografia/
│   └── ciencia-tecnologia/
├── portales/                  ← guía de portales principales
│   ├── datos-gob-mx.md
│   ├── inegi.md
│   ├── banxico.md
│   └── ...
├── herramientas/              ← snippets de código para acceder a las APIs
│   ├── python/
│   └── r/
└── docs/
    └── schema.md              ← esquema de una ficha
```

---

## Portales principales

| Portal | Institución | URL |
|--------|-------------|-----|
| datos.gob.mx | Gobierno Federal | https://datos.gob.mx |
| INEGI | Instituto Nacional de Estadística | https://www.inegi.org.mx/datos/ |
| Banxico SIE | Banco de México | https://www.banxico.org.mx/SieAPIRest/ |
| CNBV | Comisión Nacional Bancaria y de Valores | https://portafolioinfo.cnbv.gob.mx |
| SSA / DGE | Secretaría de Salud | https://www.gob.mx/salud/documentos/datos-abiertos-152127 |
| SEP | Secretaría de Educación Pública | https://www.planeacion.sep.gob.mx/estadisticaeindicadores.aspx |
| SEMARNAT | Medio ambiente | https://www.gob.mx/semarnat/documentos/datos-abiertos |
| SESNSP | Seguridad / crimen | https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva |
| CONAPO | Población y demografía | https://www.gob.mx/conapo |
| CONEVAL | Pobreza y evaluación social | https://www.coneval.org.mx/Medicion |
| SHCP | Finanzas públicas | https://www.transparenciapresupuestaria.gob.mx |
| SAT | Recaudación fiscal | https://www.sat.gob.mx/estadisticas_fiscales |

---

## Temas cubiertos

- 📊 **Economía** — PIB, comercio exterior, empleo, precios
- 🏦 **Finanzas** — tipo de cambio, tasas, sistema bancario, riesgo
- 🏥 **Salud** — epidemiología, infraestructura, mortalidad
- 🎓 **Educación** — matrícula, abandono, calidad educativa
- 🌳 **Medio ambiente** — calidad del aire, agua, biodiversidad
- 🔒 **Seguridad** — incidencia delictiva, victimización
- 👥 **Demografía** — censo, migración, proyecciones de población
- 💻 **Ciencia y tecnología** — I+D, patentes, conectividad

---

## Estado del catálogo

| Sector | Fuentes documentadas |
|--------|---------------------|
| 🏦 Finanzas | Banxico SIE, CNBV Portafolio, SHCP Transparencia |
| 📊 Economía | ENOE (INEGI), SAT Estadísticas, SHCP Presupuesto |
| 🏥 Salud | SSA/DGE Epidemiología, IMSS Trabajadores Asegurados |
| 🎓 Educación | SEP Estadísticas, MEJOREDU Indicadores |
| 🌳 Medio ambiente | SINAICA Calidad del Aire, SEMARNAT |
| 👥 Demografía | INEGI (BIE + Censo), CONAPO Proyecciones |
| 🔒 Seguridad | SESNSP Incidencia Delictiva |
| 💻 Ciencia y Tecnología | CONACYT/SECITI (ESIDET) |

_Última actualización: 2026-06-12_

---

## Cómo contribuir

Lee [CONTRIBUTING.md](CONTRIBUTING.md) para agregar nuevas fuentes o mejorar fichas existentes.

---

## Licencia

MIT — úsalo, mejóralo, compártelo.
