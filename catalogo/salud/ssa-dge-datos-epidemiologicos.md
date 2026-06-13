# SSA/DGE — Datos Abiertos Epidemiológicos

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Dirección General de Epidemiología, Secretaría de Salud |
| **Sector** | salud |
| **Periodicidad** | diaria (COVID-19, histórico); semanal (enfermedades de notificación) |
| **Última actualización** | presente |
| **Formato** | CSV (comprimido en ZIP) |
| **Licencia** | uso libre |
| **Cobertura geográfica** | nacional / estatal / municipal |
| **Cobertura temporal** | 2020 — presente |

## Descripción

La DGE publica datos de vigilancia epidemiológica a nivel de caso individual (desidentificados). El conjunto más conocido es el dataset de COVID-19 con más de 14 millones de registros. Cada registro incluye unidad médica, entidad, edad, sexo, comorbilidades, hospitalización, intubación, defunción y resultado de prueba de laboratorio.

## URL de acceso

- Portal principal: https://www.gob.mx/salud/documentos/datos-abiertos-152127
- Descarga histórica: https://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/historicos/
- Diccionario de datos: https://www.gob.mx/cms/uploads/attachment/file/600914/Descriptores_0705.pdf

## Variables principales (COVID-19)

| Variable | Tipo | Descripción |
|----------|------|-------------|
| FECHA_ACTUALIZACION | DATE | Fecha del corte de datos |
| ENTIDAD_UM | INT | Entidad de la unidad médica (clave INEGI) |
| SEXO | INT | 1=Mujer, 2=Hombre |
| EDAD | INT | Edad en años |
| MUNICIPIO_RES | INT | Municipio de residencia |
| TIPACIEN | INT | 1=Ambulatorio, 2=Hospitalizado |
| RESULTADO_LAB | INT | 1=Positivo, 2=No positivo, 3=Pendiente |
| CLASIFICACION_FINAL | INT | 1–3=COVID confirmado; 4–7=No COVID/sospechoso |
| INTUBADO | INT | 1=Sí, 2=No, 97/98/99=NA |
| DEFUNCION | INT | 1=Sí, 2=No |
| DIABETES | INT | 1=Sí, 2=No |
| HIPERTENSION | INT | 1=Sí, 2=No |

## Ejemplo de uso (Python)

```python
import pandas as pd
import zipfile
import urllib.request
from pathlib import Path

ZIP_URL = "https://datosabiertos.salud.gob.mx/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"
ZIP_PATH = Path("covid19.zip")

if not ZIP_PATH.exists():
    print("Descargando datos COVID-19 (~500 MB)...")
    urllib.request.urlretrieve(ZIP_URL, ZIP_PATH)

with zipfile.ZipFile(ZIP_PATH) as z:
    csv_name = next(f for f in z.namelist() if f.endswith(".csv"))
    chunks = pd.read_csv(
        z.open(csv_name),
        encoding="latin-1",
        low_memory=False,
        chunksize=500_000,
    )
    resultados = []
    for chunk in chunks:
        fallecidos = chunk[
            (chunk["CLASIFICACION_FINAL"].isin([1, 2, 3])) &
            (chunk["DEFUNCION"] == 1)
        ]
        resultados.append(fallecidos.groupby("ENTIDAD_RES").size())

total = pd.concat(resultados).groupby(level=0).sum().sort_values(ascending=False)
print(total.head(10))
```

## Notas de calidad

- El archivo descomprimido supera **3 GB** — siempre usar `chunksize` o filtrar con `usecols`
- Los catálogos de entidades, municipios y causas están en archivos separados dentro del mismo ZIP
- `CLASIFICACION_FINAL` es el diagnóstico definitivo; `RESULTADO_LAB` solo aplica a casos con prueba
- Desde 2023 la actualización diaria está suspendida; la serie histórica es estable y completa
- Las claves de entidad/municipio siguen la nomenclatura INEGI — cruzar con `catalogo/demografia/inegi.md`

## Referencias

- Diccionario de datos: https://www.gob.mx/cms/uploads/attachment/file/600914/Descriptores_0705.pdf
- Portal datos abiertos salud: https://datosabiertos.salud.gob.mx
- SINAVE: https://epidemiologia.salud.gob.mx
