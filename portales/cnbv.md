# CNBV — Portafolio de Información

## ¿Qué es?

El Portafolio de Información de la CNBV es la fuente oficial de estadísticas del sistema financiero mexicano: banca múltiple, banca de desarrollo, SoFiPOs, SoFoMs, uniones de crédito, casas de bolsa y Afores. Contiene indicadores prudenciales como ICAP (capitalización), IMOR (morosidad) y LCR (liquidez).

## ¿Qué datos tiene?

| Sector | Tablas principales |
|--------|-------------------|
| Banca múltiple | Balance, estado de resultados, cartera, captación, ICAP, IMOR, LCR |
| Banca de desarrollo | Balances por institución |
| SoFiPOs | Indicadores financieros por institución |
| SoFoMs | Cartera y captación |
| Casas de bolsa | Operación bursátil |
| Afores | Activos bajo administración |

## Cómo acceder

**No hay API.** Todo es descarga manual en CSV o Excel:
1. Ir a https://portafoliodeinformacion.cnbv.gob.mx
2. Navegar a "Banca Múltiple" → "Boletines Estadísticos"
3. Descargar el archivo del mes deseado (formato `BM_V.csv`, etc.)

No se requiere registro.

## Tip de navegación

Las tablas de banca múltiple se numeran BM-I a BM-VII. Para análisis rápido:
- **ICAP (capitalización):** BM-V
- **IMOR (morosidad):** BM-VI
- **Cartera total:** BM-III

## Limitaciones

- Sin API — descarga manual únicamente; no automatizable sin scraping
- Los CSVs usan **encoding Latin-1** y headers **multinivel** (filas 0-2 combinadas) — requieren limpieza
- Rezago típico: 6-8 semanas respecto al mes reportado
- Los nombres de columnas cambian ocasionalmente entre boletines

## Fichas relacionadas en este catálogo

- Ver `catalogo/finanzas/cnbv-portafolio.md` para variables clave e indicadores prudenciales
