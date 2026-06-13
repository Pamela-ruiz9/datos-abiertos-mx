# INEGI — Instituto Nacional de Estadística y Geografía

## ¿Qué es?

El INEGI es la fuente estadística más completa de México. Publica censos, encuestas, cuentas nacionales, cartografía y el Banco de Información Económica (BIE) con miles de indicadores macroeconómicos, demográficos y sociales.

A diferencia de otros portales del gobierno mexicano, el INEGI tiene una **API REST bien documentada** (BIE), datos históricos que datan desde los años 1990, y buenas prácticas de metadatos y metodología.

## ¿Qué datos tiene?

| Fuente | Tipo | Periodicidad |
|--------|------|--------------|
| Censo de Población y Vivienda | Microdatos, indicadores | Decenal (2020, 2010...) |
| ENOE | Mercado laboral, empleo | Trimestral |
| ENIGH | Ingresos y gasto de hogares | Bienal |
| INPC | Inflación, precios | Quincenal/mensual |
| PIB trimestral (CMAP) | Cuentas nacionales | Trimestral |
| DENUE | Directorio de empresas geocodificado | Semestral |
| Marco Geoestadístico | Polígonos AGEB, municipios | Anual |
| ENVIPE | Victimización y percepción de seguridad | Anual |
| BIE | +3,000 indicadores vía API | Varía |

## Cómo acceder

**API BIE (indicadores):** Requiere token gratuito.
1. Registrarse en https://www.inegi.org.mx/app/developer/
2. Obtener token por email
3. Usar la API: `GET /INDICATOR/{id}/es/{area}/false/BIE/2.0/{token}?type=json`

**Microdatos (encuestas):** Descarga directa sin registro desde cada página de programa.

**DENUE:** Descarga por estado o consulta API en https://www.inegi.org.mx/app/mapa/denue/

## Tip de navegación

Para encontrar el ID de un indicador BIE: usar el buscador en https://www.inegi.org.mx/app/api/indicadores/indiname/

## Limitaciones

- La API BIE tiene alta latencia en horas pico (7-10 am y 3-5 pm)
- Los archivos de microdatos del Censo superan 1 GB — usar `chunksize` en pandas
- Algunos indicadores históricos cambian de metodología sin aviso — revisar notas técnicas
- El DENUE puede tener registros desactualizados para empresas pequeñas

## Fichas relacionadas en este catálogo

- Ver `catalogo/demografia/inegi.md` para documentación completa de la API BIE
- Ver `catalogo/economia/enoe-empleo.md` para la ENOE específicamente
- Ver `catalogo/demografia/conapo-proyecciones.md` para proyecciones demográficas
