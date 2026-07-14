# SEMARNAT — Datos Abiertos de Medio Ambiente

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Secretaría de Medio Ambiente y Recursos Naturales |
| **Sector** | medio ambiente |
| **Periodicidad** | irregular / anual |
| **Última actualización** | presente |
| **Formato** | CSV, shapefile |
| **Licencia** | uso libre |
| **Cobertura geográfica** | nacional / estatal |
| **Cobertura temporal** | varía por dataset |

## Descripción

SEMARNAT publica datasets ambientales en datos.gob.mx: residuos sólidos, descargas de aguas residuales, licencias ambientales, impacto ambiental y áreas naturales protegidas. Para biodiversidad y especies, CONABIO complementa con capas GIS más completas.

## URL de acceso

- Portal datos abiertos: https://www.gob.mx/semarnat/documentos/datos-abiertos
- datos.gob.mx SEMARNAT: https://www.datos.gob.mx/organization/ (buscar "SEMARNAT")
- CONABIO (biodiversidad): https://www.conabio.gob.mx/informacion/gis/
- CONAGUA (agua): https://www.conagua.gob.mx/CONAGUA07/Contenido/Documentos/SINA/

## Datasets principales

| Dataset | Formato | Descripción |
|---------|---------|-------------|
| Residuos sólidos urbanos | CSV | Generación y manejo por municipio |
| Descargas de aguas residuales | CSV | Volumen y calidad por cuerpo de agua |
| Licencias ambientales (SCEIA) | CSV | Cédulas de operación anual de industria |
| Impacto ambiental | CSV | MIA autorizadas y condicionadas |
| Especies en riesgo (NOM-059) | CSV | Listado de especies protegidas con distribución |
| Áreas naturales protegidas | shapefile | Polígonos de ANPs federales |

## Variables principales (ANPs — shapefile)

| Variable | Tipo | Descripción |
|----------|------|-------------|
| NOMBRE | STR | Nombre del área natural protegida |
| CATEGORIA | STR | Tipo (Reserva Biosfera, Parque Nacional, etc.) |
| ESTADO | STR | Entidad(es) donde se ubica |
| SUPERFICIE | FLOAT | Superficie total (hectáreas) |
| DECRETO | DATE | Fecha de decreto de creación |
| geometry | GEOMETRY | Polígono del ANP |

## Ejemplo de uso (Python)

```python
import geopandas as gpd

# Shapefile de ANPs (descargar desde CONABIO o SEMARNAT)
anps = gpd.read_file("anp_fed.shp")
anps = anps.to_crs(epsg=4326)  # WGS84

# ANPs por estado y categoría
resumen = anps.groupby(["ESTADO", "CATEGORIA"]).agg(
    count=("NOMBRE", "count"),
    superficie_ha=("SUPERFICIE", "sum"),
)
print(resumen.sort_values("superficie_ha", ascending=False).head(10))
```

## Notas de calidad

- SEMARNAT no tiene API — todos los datos son descarga manual
- Los datos de descargas industriales tienen subregistro importante; muchas empresas no reportan
- Los shapefiles de ANPs están actualizados y son confiables para análisis geográfico
- Para análisis de biodiversidad, CONABIO ofrece datos más completos y geocodificados

## Referencias

- Portal SEMARNAT datos abiertos: https://www.gob.mx/semarnat/documentos/datos-abiertos
- CONABIO geoportal: https://www.conabio.gob.mx/informacion/gis/
- Sistema de Áreas Naturales Protegidas (SINAP): https://www.gob.mx/conanp/documentos/sistema-de-areas-naturales-protegidas
