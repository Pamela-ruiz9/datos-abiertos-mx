# MEJOREDU — Indicadores Nacionales de Mejora Educativa

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Comisión Nacional para la Mejora Continua de la Educación |
| **Sector** | educación |
| **Periodicidad** | anual |
| **Última actualización** | presente |
| **Formato** | Excel, PDF |
| **Licencia** | uso libre |
| **Cobertura geográfica** | nacional / estatal |
| **Cobertura temporal** | 2018 — presente |

## Descripción

MEJOREDU publica los Indicadores Nacionales de la Mejora Continua de la Educación en México. A diferencia de las estadísticas de volumen de la SEP, MEJOREDU mide calidad y equidad: logro educativo de alumnos, condiciones de aprendizaje, formación docente y eficiencia del sistema.

## URL de acceso

- Portal de indicadores: https://www.mejoredu.gob.mx/indicadores
- Publicaciones e informes: https://www.mejoredu.gob.mx/publicaciones/informe-de-resultados
- datos.gob.mx MEJOREDU: https://datos.gob.mx/busca/organization/mejoredu

## Variables principales

| Indicador | Tipo | Descripción |
|-----------|------|-------------|
| cobertura_neta | FLOAT | % de población en edad escolar matriculada |
| rezago_educativo | FLOAT | % de adultos sin educación básica completa |
| eficiencia_terminal_primaria | FLOAT | % que concluye primaria en tiempo normativo |
| eficiencia_terminal_secundaria | FLOAT | % que concluye secundaria |
| tasa_abandono_ms | FLOAT | Abandono escolar en media superior (%) |
| logro_lectura | FLOAT | % de alumnos con logro satisfactorio en lectura |
| logro_matematicas | FLOAT | % con logro satisfactorio en matemáticas |
| docentes_formacion_continua | FLOAT | % de docentes en formación continua |

## Ejemplo de uso (Python)

```python
import pandas as pd

# Los datos de MEJOREDU se publican en Excel descargable desde el portal
# No hay API — descarga manual requerida
df = pd.read_excel("indicadores_mejoredu_2023.xlsx", sheet_name="Indicadores", header=2)
df = df.dropna(subset=["Entidad"])

# Comparar logro educativo en matemáticas por estado
print(df[["Entidad", "logro_matematicas"]].sort_values("logro_matematicas", ascending=False))
```

## Notas de calidad

- No hay API — todos los datos son descarga manual desde el portal
- MEJOREDU sustituyó al INEE en 2019 — para comparaciones con años anteriores, buscar publicaciones del INEE (2013-2019)
- Los exámenes Planea (INEE) fueron reemplazados por otros instrumentos a partir de 2022 — las series no son directamente comparables
- Los indicadores de logro educativo tienen cobertura parcial: no todos los estados participan en todas las evaluaciones

## Referencias

- Indicadores nacionales: https://www.mejoredu.gob.mx/indicadores
- INEE (datos históricos 2013-2019): https://www.inee.edu.mx/evaluaciones/
- SEP estadísticas de volumen: https://www.planeacion.sep.gob.mx/estadisticaeindicadores.aspx
