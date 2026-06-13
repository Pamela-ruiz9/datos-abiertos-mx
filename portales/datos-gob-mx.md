# datos.gob.mx — Portal Nacional de Datos Abiertos

## ¿Qué es?

datos.gob.mx es el metaportal oficial del gobierno federal mexicano. Agrega datasets de más de 300 dependencias federales: secretarías, organismos autónomos, empresas paraestatales y gobiernos estatales adheridos.

Es un portal CKAN — el mismo estándar de portales de datos abiertos usado por EUA, Reino Unido y la Unión Europea — lo que significa que tiene una API estándar para buscar y acceder a datasets programáticamente.

El volumen supera los 18,000 datasets, pero la calidad y actualización varía enormemente por dependencia.

## ¿Qué datos tiene?

| Tema | Ejemplo de datasets |
|------|---------------------|
| Salud | Registros epidemiológicos IMSS, SSA |
| Educación | Escuelas y matrícula SEP, Formato 911 |
| Economía | Trabajadores asegurados IMSS, recaudación SAT |
| Seguridad | Incidencia delictiva SESNSP |
| Geografía | Límites territoriales, cartografía INEGI |
| Gobierno | Declaraciones patrimoniales, contratos |
| Medio ambiente | Residuos, descargas SEMARNAT |

## Cómo acceder

No requiere registro. Todo es descarga libre.

**Descarga manual:** Buscar dataset → click en recurso → descargar CSV/XLS

**API CKAN (programática):**
```python
import requests

BASE = "https://datos.gob.mx/api/3/action"

# Buscar datasets por término
r = requests.get(f"{BASE}/package_search", params={"q": "trabajadores imss", "rows": 5})
r.raise_for_status()
results = r.json()["result"]["results"]
for ds in results:
    print(ds["title"], "—", ds["organization"]["title"])
```

## Tip de navegación

Usar el filtro **Organización** para ir directo a una dependencia. El buscador de texto libre devuelve muchos resultados irrelevantes.

URL directa a organización: `https://datos.gob.mx/busca/organization/[slug-dependencia]`
Ej: `https://datos.gob.mx/busca/organization/imss`

## Limitaciones

- Muchos datasets están desactualizados — verificar la fecha de última actualización antes de usar
- El mismo dataset puede existir en múltiples versiones (por año); no siempre hay un dataset "live"
- La API CKAN devuelve metadatos, no los datos en sí — para los datos hay que seguir el enlace al recurso
- Algunos datasets son solo PDFs o links rotos

## Fichas relacionadas en este catálogo

- Ver `catalogo/salud/imss-estadisticas.md` para trabajadores asegurados IMSS
- Ver `catalogo/seguridad/sesnsp-incidencia-delictiva.md` para datos del SESNSP
