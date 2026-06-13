# SESNSP — Datos Abiertos de Incidencia Delictiva

## ¿Qué es?

El Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública (SESNSP) publica mensualmente estadísticas de incidencia delictiva del fuero común y federal. Es la principal fuente oficial de estadísticas de crimen en México, aunque refleja solo los delitos denunciados (la cifra negra se estima en 90%+).

## ¿Qué datos tiene?

| Dataset | Granularidad | Cobertura |
|---------|-------------|-----------|
| Incidencia delictiva fuero común | Nacional / estatal / municipal | 2015–presente |
| Incidencia delictiva fuero federal | Nacional / estatal | 2015–presente |
| Víctimas del fuero común | Nacional / estatal / municipal | 2015–presente |
| Llamadas de emergencia 9-1-1 | Municipal | 2016–presente |
| Feminicidios | Nacional / estatal | 2015–presente |

## Cómo acceder

Sin registro. Descarga directa desde Google Drive (archivos CSV mensuales acumulados):
- Portal: https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva
- Los archivos se llaman `IDEFC_NM_MMMAA.csv` (ej. `IDEFC_NM_abr24.csv`)

## Tip de navegación

Descargar el archivo más reciente que incluye el histórico acumulado desde 2015. No es necesario descargar archivos de años anteriores por separado.

```python
import pandas as pd
df = pd.read_csv("IDEFC_NM_abr24.csv", encoding="latin-1")
```

## Limitaciones

- Los datos reflejan **carpetas de investigación abiertas**, no delitos reales
- La cifra negra se estima en 90%+ — usar la **ENVIPE** (encuesta INEGI) para estimar delitos reales
- Los municipios pequeños pueden tener subregistro significativo
- La metodología cambió en 2015 — no comparar directamente con datos anteriores

## Fichas relacionadas en este catálogo

- Ver `catalogo/seguridad/sesnsp-incidencia-delictiva.md` para documentación completa y snippet de análisis
