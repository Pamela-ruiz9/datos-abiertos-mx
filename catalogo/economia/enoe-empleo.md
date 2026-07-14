# INEGI ENOE — Encuesta Nacional de Ocupación y Empleo

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | INEGI |
| **Sector** | economía / empleo |
| **Periodicidad** | trimestral |
| **Última actualización** | presente |
| **Formato** | CSV (microdatos), API BIE (indicadores agregados) |
| **Licencia** | uso libre con atribución |
| **Cobertura geográfica** | nacional / estatal (indicadores); hogar/individuo (microdatos) |
| **Cobertura temporal** | 2005 — presente |

## Descripción

La ENOE es la principal fuente de estadísticas laborales de México. Mide trimestralmente la tasa de desocupación, subocupación, informalidad y condiciones de empleo para la población de 15 años y más. Publica indicadores agregados (API BIE) y microdatos del cuestionario.

## URL de acceso

- Portal ENOE: https://www.inegi.org.mx/programas/enoe/15ymas/
- Microdatos (descarga): https://www.inegi.org.mx/programas/enoe/15ymas/#Microdatos
- API BIE token (gratuito): https://www.inegi.org.mx/app/developer/

## Indicadores BIE clave

| ID | Descripción |
|----|-------------|
| 444612 | Tasa de desocupación nacional (%) |
| 444637 | Tasa de subocupación (%) |
| 444656 | Tasa de informalidad laboral (%) |
| 493856 | Población económicamente activa (miles) |

## Variables principales (microdatos — SDEM)

| Variable | Tipo | Descripción |
|----------|------|-------------|
| ent | INT | Entidad federativa |
| sex | INT | Sexo (1=H, 2=M) |
| eda | INT | Edad |
| clase1 | INT | Condición de actividad (1=PEA, 2=PNEA) |
| clase2 | INT | Desocupados (1) vs Ocupados (2) dentro de PEA |
| fac | FLOAT | Factor de expansión (ponderador muestral) |
| per | STR | Periodo (trimestre/año) |

## Ejemplo de uso (Python)

```python
import requests

TOKEN = "tu_token_inegi"
INDICADOR = "444612"  # Tasa de desocupación

url = (
    f"https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml"
    f"/INDICATOR/{INDICADOR}/es/0700/false/BIE/2.0/{TOKEN}?type=json"
)
r = requests.get(url)
r.raise_for_status()

for o in r.json()["Series"][0]["OBSERVATIONS"][-8:]:
    print(o["TIME_PERIOD"], o["OBS_VALUE"])
```

## Notas de calidad

- Los microdatos usan diseño muestral complejo — usar `fac` (factor de expansión) para estimaciones representativas
- El diseño muestral cambió en 2020 (ENOE Nueva Edición) — no comparar directamente con años anteriores sin ajuste metodológico
- La API BIE puede tardar varios segundos en horas pico; implementar reintento con backoff
- Las series estatales tienen mayor error estándar que las nacionales

## Referencias

- Metodología ENOE: https://www.inegi.org.mx/programas/enoe/15ymas/
- Nota ENOE Nueva Edición: https://www.inegi.org.mx/contenidos/programas/enoe/15ymas/doc/nota_nueva_enoe.pdf
- Catálogo indicadores BIE: https://www.inegi.org.mx/app/indicadores/
