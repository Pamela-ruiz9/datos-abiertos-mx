# SHCP — Transparencia Presupuestaria

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Secretaría de Hacienda y Crédito Público |
| **Sector** | finanzas públicas / economía |
| **Periodicidad** | mensual |
| **Última actualización** | presente |
| **Formato** | CSV, JSON (API REST) |
| **Licencia** | uso libre |
| **Cobertura geográfica** | federal |
| **Cobertura temporal** | 2001 — presente |

## Descripción

Transparencia Presupuestaria es el portal de rendición de cuentas del gasto público federal. Publica el Presupuesto de Egresos de la Federación (PEF) aprobado, modificado, devengado y ejercido, a nivel programa presupuestario, dependencia, función y proyecto de inversión.

Permite analizar la composición y evolución del gasto público, monitorear proyectos de inversión (Cartera SHCP) y comparar asignaciones aprobadas vs. gasto real mes a mes.

## URL de acceso

- Portal: https://www.transparenciapresupuestaria.gob.mx
- API Open Data: https://www.transparenciapresupuestaria.gob.mx/ptp/contenido/api
- Descarga PEF (CSV/XLS): https://www.transparenciapresupuestaria.gob.mx/ptp/contenido/descargaInfo
- Cartera de inversión: https://www.transparenciapresupuestaria.gob.mx/ptp/contenido/API/cartera

## Variables principales

| Variable | Tipo | Descripción |
|----------|------|-------------|
| ciclo | INT | Año del ejercicio fiscal |
| desc_dependencia | STR | Secretaría o entidad |
| desc_ur | STR | Unidad Responsable |
| desc_pp | STR | Programa Presupuestario |
| cve_fun | STR | Clave de Función del gasto |
| monto_aprobado | FLOAT | PEF aprobado por Cámara de Diputados (pesos) |
| monto_modificado | FLOAT | PEF tras adecuaciones presupuestarias |
| monto_devengado | FLOAT | Gasto comprometido y reconocido contablemente |
| monto_ejercido | FLOAT | Gasto efectivamente pagado |

## Ejemplo de uso (Python)

```python
import requests
import pandas as pd
from io import StringIO

# Descarga del PEF ejercido (CSV dinámico)
# Verificar parámetros actualizados en la documentación de la API
url = "https://www.transparenciapresupuestaria.gob.mx/ptp/contenido/api"
params = {"type": "egresos", "anio": 2024}
r = requests.get(url, params=params, timeout=60)
r.encoding = "latin-1"

df = pd.read_csv(StringIO(r.text), low_memory=False)
resumen = (
    df.groupby("desc_dependencia")["monto_ejercido"]
    .sum()
    .sort_values(ascending=False)
)
print(resumen.head(10))
```

## Notas de calidad

- Montos en **pesos corrientes** del año — deflactar con INPC para comparaciones históricas
- `devengado` ≠ `ejercido` en diciembre: el devengado incluye compromisos pendientes de pago al 31 de diciembre
- La Cartera SHCP solo cubre proyectos de inversión ≥ 100 MDP; proyectos menores no aparecen
- CSVs en encoding **Latin-1** con comas como separador de miles
- La estructura de la API puede cambiar entre ejercicios fiscales — verificar el diccionario vigente cada año

## Referencias

- Diccionario de datos API: https://www.transparenciapresupuestaria.gob.mx/ptp/contenido/api/diccionario
- Ley de Presupuesto y Responsabilidad Hacendaria: https://www.diputados.gob.mx/LeyesBiblio/pdf/LPRH.pdf
- Cuenta Pública (cierre anual): https://www.transparenciapresupuestaria.gob.mx/es/PTP/cp
