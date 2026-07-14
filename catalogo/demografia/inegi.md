# INEGI — Instituto Nacional de Estadística y Geografía

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | INEGI |
| **Sector** | demografía / economía / geografía / salud / educación |
| **Periodicidad** | varía (mensual, trimestral, quinquenal, censal) |
| **Última actualización** | presente |
| **Formato** | CSV, JSON (API INEGI), Excel, shapefile (geografía) |
| **Licencia** | uso libre con atribución |
| **Cobertura geográfica** | nacional / estatal / municipal / AGEB |
| **Cobertura temporal** | varía (algunos desde 1990) |

## Descripción

INEGI es la fuente estadística más completa de México. Publica el Censo de Población, encuestas (ENOE, ENIGH, ENVIPE), cuentas nacionales, estadísticas de comercio exterior, precios al consumidor y más.

Tiene **API abierta** (BIE — Banco de Información Económica) con miles de indicadores.

## URL de acceso

- Portal general: https://www.inegi.org.mx/datos/
- API BIE: `https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/{indicador}/es/0700/false/BIE/2.0/{token}?type=json`
- Token API (gratuito): https://www.inegi.org.mx/app/developer/
- Datos abiertos (descarga): https://www.inegi.org.mx/datos/?t=0060

## Fuentes principales

| Fuente | Descripción | Periodicidad |
|--------|-------------|--------------|
| Censo de Población y Vivienda | Demografía completa nacional | Decenal (2020, 2010...) |
| ENOE | Encuesta Nacional de Ocupación y Empleo | Trimestral |
| ENIGH | Encuesta Nacional de Ingresos y Gastos | Bienal |
| INPC | Índice Nacional de Precios al Consumidor | Quincenal/mensual |
| CMAP | Cuentas Nacionales / PIB | Trimestral |
| ENVIPE | Encuesta Nacional de Victimización | Anual |
| Directorio Estadístico de Unidades Económicas (DENUE) | Empresas geocodificadas | Semestral |
| Marco Geoestadístico | Polígonos AGEB, municipios, estados | Anual |

## Indicadores BIE frecuentes

| Indicador | Descripción |
|-----------|-------------|
| 444612 | Tasa de desocupación nacional |
| 216064 | PIB trimestral (millones pesos 2013) |
| 628229 | Variación anual del INPC |
| 383179 | Pobreza extrema (CONEVAL vía INEGI) |

## Ejemplo de uso (Python)

```python
import requests

TOKEN = "tu_token_inegi"
INDICADOR = "444612"  # tasa de desocupación

url = (
    f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml"
    f"/INDICATOR/{INDICADOR}/es/0700/false/BIE/2.0/{TOKEN}?type=json"
)

r = requests.get(url)
data = r.json()
obs = data["Series"][0]["OBSERVATIONS"]
for o in obs[-5:]:
    print(o["TIME_PERIOD"], o["OBS_VALUE"])
```

## Notas de calidad

- La API BIE puede tener latencia alta en horas pico
- Los archivos de microdatos del Censo son grandes (>1 GB) — usar `chunksize` en pandas
- El DENUE se actualiza semestralmente pero puede tener registros desactualizados
- Algunos indicadores históricos cambian de metodología — revisar notas técnicas

## Referencias

- Catálogo de indicadores BIE: https://www.inegi.org.mx/app/indicadores/
- Metodología ENOE: https://www.inegi.org.mx/programas/enoe/15ymas/
