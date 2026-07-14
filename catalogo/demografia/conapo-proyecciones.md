# CONAPO — Proyecciones de Población

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Consejo Nacional de Población |
| **Sector** | demografía |
| **Periodicidad** | quinquenal (revisión) |
| **Última actualización** | 2023 |
| **Formato** | CSV, Excel |
| **Licencia** | uso libre |
| **Cobertura geográfica** | nacional / estatal / municipal |
| **Cobertura temporal** | 1950 — 2070 |

## Descripción

CONAPO publica proyecciones demográficas de México con horizonte hasta 2070. La base incorpora resultados del Censo de Población 2020 y modela nacimientos, defunciones y migración (interna e internacional). Es la fuente oficial para análisis de estructura poblacional, envejecimiento y migración.

## URL de acceso

- Portal CONAPO: https://www.gob.mx/conapo
- Proyecciones 2020-2070: https://www.gob.mx/conapo/acciones-y-programas/conciliacion-demografica-de-mexico-1950-a-2019-y-proyecciones-de-la-poblacion-de-mexico-y-de-las-entidades-federativas-2020-a-2070-226173
- datos.gob.mx CONAPO: https://www.datos.gob.mx/organization/conapo

## Variables principales

| Variable | Tipo | Descripción |
|----------|------|-------------|
| AÑO | INT | Año de la proyección |
| ENTIDAD | INT | Clave INEGI de entidad federativa (0=nacional) |
| NOM_ENT | STR | Nombre del estado |
| SEXO | INT | 1=Hombres, 2=Mujeres, 3=Total |
| EDAD | INT | Edad en años (0–130) |
| POBINICIO | INT | Población al inicio del año |
| NACIMIENTOS | INT | Nacimientos proyectados |
| DEFUNCIONES | INT | Defunciones proyectadas |
| MIGRACION_NETA | INT | Migración neta (interna + internacional) |
| POBFIN | INT | Población al final del año |

## Ejemplo de uso (Python)

```python
import pandas as pd

# Descargar CSV desde el portal CONAPO
df = pd.read_csv("pob_muj_quinquenal.csv", encoding="latin-1")

# Pirámide poblacional nacional para 2030
pob_2030 = df[(df["AÑO"] == 2030) & (df["ENTIDAD"] == 0)]
pivot = pob_2030.pivot_table(
    index="EDAD", columns="SEXO", values="POBMITAD", aggfunc="sum"
)
print(pivot.tail(20))
```

## Notas de calidad

- Las proyecciones municipales tienen mayor incertidumbre que las estatales y nacionales
- La base 2020 fue revisada con resultados del Censo 2020 — las series anteriores a 2020 son retroproyecciones
- Para migración internacional, complementar con datos del INM
- Los archivos por sexo y grupo quinquenal están separados — requieren merge para análisis integrado

## Referencias

- Metodología de proyecciones: https://www.gob.mx/conapo/acciones-y-programas/conciliacion-demografica-2020-2070
- Censo de Población 2020 (base): https://www.inegi.org.mx/programas/ccpv/2020/
- CONAPO indicadores demográficos: https://www.datos.gob.mx/dataset/ (buscar "indicadores demográficos")
