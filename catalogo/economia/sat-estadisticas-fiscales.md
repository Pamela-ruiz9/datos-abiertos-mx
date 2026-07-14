# SAT — Estadísticas Fiscales

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Servicio de Administración Tributaria |
| **Sector** | economía / finanzas públicas |
| **Periodicidad** | mensual (recaudación); anual (anuarios estadísticos) |
| **Última actualización** | presente |
| **Formato** | Excel, PDF |
| **Licencia** | uso libre |
| **Cobertura geográfica** | nacional |
| **Cobertura temporal** | 2000 — presente |

## Descripción

El SAT publica estadísticas de recaudación tributaria federal: ISR, IVA, IEPS y otros impuestos. Incluye reportes mensuales de ingresos tributarios comparados con la Ley de Ingresos de la Federación (LIF), y anuarios con datos de contribuyentes, devoluciones y créditos fiscales.

## URL de acceso

- Estadísticas generales: https://www.sat.gob.mx/estadisticas_fiscales
- Cifras SAT (ingresos mensuales): https://www.sat.gob.mx/cifras_sat
- Anuario estadístico: https://www.sat.gob.mx/consulta/23972/conoce-las-estadisticas-de-recaudacion-del-sat

## Variables principales

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Periodo | STR | Mes y año |
| ISR | FLOAT | Impuesto Sobre la Renta (millones de pesos) |
| IVA | FLOAT | Impuesto al Valor Agregado (mdp) |
| IEPS | FLOAT | Impuesto Especial sobre Producción y Servicios (mdp) |
| IEPS_Gasolinas | FLOAT | IEPS específico a gasolinas y diésel |
| Importaciones | FLOAT | Impuestos al comercio exterior (mdp) |
| Total_Tributarios | FLOAT | Total recaudación tributaria (mdp) |
| Meta_LIF | FLOAT | Meta de recaudación según LIF |
| Variacion_Real | FLOAT | Variación % real vs. año anterior |

## Ejemplo de uso (Python)

```python
import pandas as pd

# Descargar manualmente desde https://www.sat.gob.mx/cifras_sat
# Los archivos Excel tienen múltiples hojas y encabezados en fila 3-4
df = pd.read_excel(
    "recaudacion_mensual.xlsx",
    sheet_name="Recaudacion",
    header=3,
    thousands=",",
)
df = df.dropna(subset=["Periodo"])
df["Periodo"] = pd.to_datetime(df["Periodo"], format="%m/%Y", errors="coerce")
df = df[df["Periodo"].notna()]

df["pct_ISR"] = df["ISR"] / df["Total_Tributarios"] * 100
print(df[["Periodo", "Total_Tributarios", "pct_ISR"]].tail(12))
```

## Notas de calidad

- Los Excels del SAT tienen formato inconsistente entre años — los nombres de columna y filas de encabezado cambian; revisar antes de leer
- Montos en **millones de pesos corrientes** — deflactar para comparaciones históricas
- El IEPS de gasolinas es volátil: depende del precio internacional del petróleo y del tipo de cambio
- No confundir recaudación tributaria con ingresos totales del sector público (que incluye PEMEX, CFE, deuda)

## Referencias

- Ingresos del sector público: https://www.hacienda.gob.mx/POLITICAFINANCIERA/FINANZASPUBLICAS/Estadisticas_Oportunas_Finanzas_Publicas/Paginas/unica2.aspx
- Ley de Ingresos de la Federación vigente: https://www.diputados.gob.mx/LeyesBiblio/pdf/LIF_2026.pdf
