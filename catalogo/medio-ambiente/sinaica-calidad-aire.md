# SINAICA — Sistema Nacional de Información de la Calidad del Aire

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Instituto Nacional de Ecología y Cambio Climático (INECC) |
| **Sector** | medio ambiente |
| **Periodicidad** | horaria (tiempo real) |
| **Última actualización** | presente |
| **Formato** | CSV (descarga por estación), consulta web |
| **Licencia** | uso libre |
| **Cobertura geográfica** | nacional (redes estatales y municipales) |
| **Cobertura temporal** | varía por estación (algunas desde 1990s) |

## Descripción

SINAICA agrega datos de las redes de monitoreo de calidad del aire de todo México (RAMA CDMX, SIMA Monterrey, redes estatales). Permite consultar y descargar datos horarios de contaminantes atmosféricos por estación. Es la fuente oficial para análisis de calidad del aire y alertas ambientales a nivel nacional.

## URL de acceso

- Portal principal: https://sinaica.inecc.gob.mx/
- Consulta de datos por estación: https://sinaica.inecc.gob.mx/pags/datos.php
- Catálogo de estaciones: https://sinaica.inecc.gob.mx/pags/estaciones.php

## Variables principales

| Variable | Tipo | Descripción |
|----------|------|-------------|
| estacion_id | INT | ID de la estación de monitoreo |
| nombre_estacion | STR | Nombre de la estación |
| red | STR | Red de monitoreo (ej. RAMA CDMX, SIMA Monterrey) |
| estado | STR | Entidad federativa |
| lat | FLOAT | Latitud |
| lon | FLOAT | Longitud |
| fecha | DATE | Fecha de medición |
| hora | INT | Hora (0–23, UTC-6) |
| PM10 | FLOAT | Material particulado ≤10 µm (µg/m³) |
| PM25 | FLOAT | Material particulado ≤2.5 µm (µg/m³) |
| O3 | FLOAT | Ozono (ppm) |
| NO2 | FLOAT | Dióxido de nitrógeno (ppm) |
| SO2 | FLOAT | Dióxido de azufre (ppm) |
| CO | FLOAT | Monóxido de carbono (ppm) |

## Ejemplo de uso (Python)

```python
import requests
import pandas as pd
from io import StringIO

# Descarga de datos horarios por estación vía formulario web
url = "https://sinaica.inecc.gob.mx/pags/datos.php"
params = {
    "estacionId": "1",   # Ejemplo: CDMX Pedregal
    "parametro": "PM25",
    "fechaIni": "2024-01-01",
    "fechaFin": "2024-01-31",
}
r = requests.post(url, data=params, timeout=30)
r.raise_for_status()
df = pd.read_csv(StringIO(r.text))
print(df.describe())
```

## Notas de calidad

- No todas las estaciones miden todos los contaminantes — verificar disponibilidad en el catálogo de estaciones
- Los datos tienen gaps frecuentes por mantenimiento de equipo; es normal encontrar valores faltantes
- El índice IMECA/ICA se calcula a partir de los contaminantes pero SINAICA no lo publica directamente
- Para CDMX, la red RAMA tiene portal propio con datos más completos y en tiempo real: http://www.aire.cdmx.gob.mx/
- La API del portal es no-oficial (formulario web) — puede cambiar sin aviso

## Referencias

- Portal SINAICA: https://sinaica.inecc.gob.mx/
- Red RAMA CDMX: http://www.aire.cdmx.gob.mx/
- Normas de calidad del aire (NOM): https://www.gob.mx/inecc/acciones-y-programas/normas-oficiales-mexicanas-nom
