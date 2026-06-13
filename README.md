# 📚 Diccionario de Datos Abiertos — México

> Un mapa de qué existe, dónde está, qué contiene y cómo usarlo.

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
| CNBV | Comisión Nacional Bancaria y de Valores | https://portafoliodeinformacion.cnbv.gob.mx |
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
