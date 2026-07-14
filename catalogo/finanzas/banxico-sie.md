# Banxico SIE — Sistema de Información Económica

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Banco de México |
| **Sector** | finanzas / economía |
| **Periodicidad** | diaria / mensual / trimestral (depende de la serie) |
| **Última actualización** | presente |
| **Formato** | JSON (API REST) |
| **Licencia** | uso libre con registro de token |
| **Cobertura geográfica** | nacional |
| **Cobertura temporal** | varía por serie (algunas desde 1990s) |

## Descripción

El SIE de Banxico es la principal fuente de series macroeconómicas y financieras de México. Cubre tipo de cambio, tasas de interés, inflación, agregados monetarios, balanza de pagos, crédito bancario y más.

Requiere token gratuito: https://www.banxico.org.mx/SieAPIRest/service/v1/token

## URL de acceso

- Portal: https://www.banxico.org.mx/SieAPIRest/
- API base: `https://www.banxico.org.mx/SieAPIRest/service/v1/series/{serie}/datos`
- Catálogo de series: https://www.banxico.org.mx/SieAPIRest/service/v1/doc/consultaSeries

## Series más usadas

| Serie | Descripción |
|-------|-------------|
| SF43718 | Tipo de cambio FIX (MXN/USD) |
| SF61745 | Tasa de interés objetivo (TIIE 28 días) |
| SP68257 | Inflación mensual (INPC) |
| SF46410 | Reservas internacionales |
| SF3367 | TIIE 91 días |
| SF43773 | Tipo de cambio interbancario 48 hrs |
| SG185 | Base monetaria |
| SF43707 | Reservas en USD |

## Ejemplo de uso (Python)

```python
import requests

TOKEN = "tu_token_aqui"
SERIE = "SF43718"  # FIX

url = f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/{SERIE}/datos/oportuno"
headers = {"Bmx-Token": TOKEN}

r = requests.get(url, headers=headers)
data = r.json()

serie = data["bmx"]["series"][0]
obs = serie["datos"][0]
print(f"{obs['fecha']}: {obs['dato']} MXN/USD")
```

## Notas de calidad

- El token es gratuito pero se gestiona por correo institucional de Banxico
- Límite: 10,000 consultas/día por token
- Las series históricas a veces tienen gaps o cambios metodológicos — revisar documentación de cada serie
- La tasa objetivo (SF61745) puede aparecer vacía en fines de semana — usar `datos/oportuno` en lugar de `datos` para el valor más reciente

## Referencias

- Documentación API: https://www.banxico.org.mx/SieAPIRest/service/v1/doc/consultaSeries
- Catálogo completo de series: https://www.banxico.org.mx/SieAPIRest/service/v1/doc/consultaSeries
