# SESNSP — Incidencia Delictiva

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública |
| **Sector** | seguridad |
| **Periodicidad** | mensual |
| **Última actualización** | presente (con rezago ~1 mes) |
| **Formato** | CSV, Excel |
| **Licencia** | uso libre |
| **Cobertura geográfica** | nacional / estatal / municipal |
| **Cobertura temporal** | 2015 — presente |

## Descripción

El SESNSP publica estadísticas de incidencia delictiva del fuero común y federal a nivel nacional, estatal y municipal. Incluye carpetas de investigación, víctimas por tipo de delito, llamadas de emergencia al 9-1-1, y datos de feminicidios.

## URL de acceso

- Portal: https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva
- Descarga directa (fuero común): https://drive.google.com/drive/folders/1pHscFsQFkzBMBqSrPlTHFkNGnXFnpL8R

## Datasets disponibles

| Dataset | Descripción |
|---------|-------------|
| Incidencia delictiva fuero común | Carpetas de investigación por tipo de delito, estado, municipio |
| Incidencia delictiva fuero federal | Delitos federales |
| Víctimas del fuero común | Número de víctimas (no carpetas) |
| Llamadas de emergencia 9-1-1 | Volumen de llamadas y tipo |
| Feminicidios | Serie específica de feminicidios |

## Variables principales

| Variable | Descripción |
|----------|-------------|
| año | Año del delito |
| mes | Mes (enero–diciembre) |
| entidad | Estado |
| municipio | Municipio |
| bien_juridico_afectado | Categoría del delito |
| tipo_de_delito | Subcategoría |
| subtipo_de_delito | Detalle |
| modalidad | Modalidad específica |
| enero–diciembre | Número de carpetas por mes |

## Ejemplo de uso (Python)

```python
import pandas as pd

df = pd.read_csv("IDEFC_NM_abr24.csv", encoding="latin-1")

# Homicidios dolosos por estado en 2023
hom = df[
    (df["tipo_de_delito"] == "Homicidio") &
    (df["modalidad"] == "Doloso") &
    (df["año"] == 2023)
]
resumen = hom.groupby("entidad")[["enero","febrero","marzo"]].sum()
print(resumen)
```

## Notas de calidad

- Los datos reflejan **carpetas de investigación abiertas**, no delitos reales (cifra negra estimada en 90%+)
- Los municipios pequeños pueden tener subregistro significativo
- La metodología cambió en 2015 — no comparar directamente con datos anteriores
- Para comparaciones históricas largas, usar la ENVIPE (encuesta de victimización) del INEGI

## Referencias

- Metodología SESNSP: https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva
- ENVIPE (para cifra negra): https://www.inegi.org.mx/programas/envipe/
