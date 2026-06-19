# DataMexico — Plataforma de Visualización de Datos

## ¿Qué es?

DataMexico es una plataforma de visualización interactiva desarrollada por Datawheel en colaboración con la Secretaría de Economía (SE). Agrega y presenta datos económicos, sociales y demográficos de México en gráficas y mapas listos para consumir, a nivel nacional, estatal y municipal.

A diferencia del resto de portales en este catálogo (que exponen datos crudos), DataMexico es una **capa de presentación** sobre esos mismos datos — transforma fuentes como INEGI, IMSS, SAT y SE en visualizaciones navegables sin necesidad de código. Tiene además una **API Tesseract** no oficial que permite consultar los cubos de datos directamente.

## ¿Qué datos tiene?

| Tema | Ejemplos de indicadores |
|------|------------------------|
| Economía | PIB por sector, valor agregado, productividad |
| Comercio exterior | Exportaciones e importaciones por producto y destino (HS6) |
| Empleo | Trabajadores asegurados IMSS por municipio y sector |
| Demografía | Población, migración, estructura por edad |
| Educación | Matrícula, abandono, eficiencia terminal |
| Salud | Mortalidad, infraestructura médica |
| Geografía | Perfiles por estado y municipio |

## Cómo acceder

**Portal web (sin registro):**
- URL SE: https://www.economia.gob.mx/datamexico/es/
- Navegar a perfiles por estado, municipio, sector o producto

**API Tesseract (no oficial, sin token):**
```python
import requests
import pandas as pd

# Ejemplo: trabajadores asegurados IMSS por estado
url = "https://api.datamexico.org/tesseract/data.jsonrecords"
params = {
    "cube": "imss_jobsbyestablishment",
    "drilldowns": "State",
    "measures": "Workers",
    "parents": "true",
}
r = requests.get(url, params=params, timeout=30)
r.raise_for_status()
body = r.json()
if "error" in body:
    raise ValueError(f"Tesseract API error: {body['error']}")
df = pd.DataFrame(body["data"])
print(df.sort_values("Workers", ascending=False).head(10))
```

## Tip de navegación

Para explorar los cubos disponibles en la API:
```
GET https://api.datamexico.org/tesseract/cubes
```
Devuelve un JSON con todos los cubos, sus dimensiones y medidas disponibles.

Para perfiles geográficos rápidos, la URL sigue el patrón:
`https://www.economia.gob.mx/datamexico/es/profile/geo/{slug-estado}`

## Limitaciones

- La API Tesseract **no es oficial** — no tiene documentación pública ni SLA; puede cambiar sin aviso
- Los datos son procesados y agregados: no son microdatos crudos; para análisis propios, ir a la fuente primaria
- La plataforma web es una SPA pesada (React + D3) — no se puede scraper fácilmente
- La cobertura temporal varía por cubo; algunos no tienen series largas
- No todos los indicadores visibles en el portal están disponibles en la API

## Diferencia con este catálogo

DataMexico muestra **el resultado**; este catálogo documenta **los ingredientes**. Si ves algo interesante en DataMexico y quieres reproducirlo, profundizar o automatizarlo, las fichas de `catalogo/` apuntan a las fuentes primarias originales.

## Fichas relacionadas en este catálogo

- `catalogo/finanzas/banxico-sie.md` — series macroeconómicas
- `catalogo/economia/enoe-empleo.md` — empleo IMSS / ENOE
- `catalogo/demografia/inegi.md` — demografía INEGI
- `catalogo/economia/shcp-transparencia-presupuestaria.md` — gasto público
