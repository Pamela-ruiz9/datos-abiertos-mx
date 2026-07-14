# CNBV — Portafolio de Información

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Comisión Nacional Bancaria y de Valores |
| **Sector** | finanzas / sistema bancario |
| **Periodicidad** | mensual (con rezago ~2 meses) |
| **Última actualización** | mensual |
| **Formato** | CSV (descarga manual), Excel |
| **Licencia** | uso libre |
| **Cobertura geográfica** | nacional |
| **Cobertura temporal** | 2000 — presente |

## Descripción

El Portafolio de Información de la CNBV contiene estadísticas del sistema financiero mexicano: banca múltiple, banca de desarrollo, SoFiPOs, SoFoMs, uniones de crédito, casas de bolsa, y más.

Es la fuente oficial para indicadores prudenciales: ICAP, LCR, IMOR, NSFR, y estadísticas de captación y cartera.

## URL de acceso

- Portal: https://portafolioinfo.cnbv.gob.mx
- Banca múltiple: https://portafolioinfo.cnbv.gob.mx/PUBLICACIONES/Boletines/Paginas/default.aspx
- SoFiPOs: https://portafolioinfo.cnbv.gob.mx/PUBLICACIONES/Boletines/Paginas/SOFIPOS.aspx

## Tablas principales (Banca Múltiple)

| Tabla | Descripción |
|-------|-------------|
| BM-I | Balance general consolidado |
| BM-II | Estado de resultados |
| BM-III | Cartera de crédito |
| BM-IV | Captación |
| BM-V | Índice de capitalización (ICAP) |
| BM-VI | Cartera vencida (IMOR) |
| BM-VII | Liquidez (LCR / CCL) |

## Variables clave

| Variable | Descripción |
|----------|-------------|
| ICAP | Índice de Capitalización — capital / activos ponderados por riesgo (mín. requerido: 10.5%) |
| IMOR | Índice de Morosidad — cartera vencida / cartera total |
| LCR | Liquidity Coverage Ratio (req. mínimo: 100%) |
| NSFR / CFEN | Net Stable Funding Ratio |
| ROA / ROE | Rentabilidad sobre activos / capital |

## Notas de calidad

- Los CSVs usan encoding **Latin-1** — leer con `encoding='latin-1'` en Python
- Los headers son **multinivel** (filas 0-2 combinadas) — requieren limpieza manual
- El rezago típico es de 6-8 semanas respecto al mes reportado
- No tienen API — descarga manual o scraping del portal

## Ejemplo de uso (Python)

```python
import pandas as pd

# Los CSVs de CNBV tienen encoding Latin-1 y headers multinivel
df = pd.read_csv("BM_V.csv", encoding="latin-1", header=[0,1,2], thousands=",")
# Limpiar headers multinivel antes de usar
df.columns = ["_".join([c for c in col if "Unnamed" not in str(c)]).strip() 
              for col in df.columns]
```

## Referencias

- Metodología CNBV: https://portafolioinfo.cnbv.gob.mx
- Glosario de términos: https://portafolioinfo.cnbv.gob.mx/Paginas/glosario.aspx
