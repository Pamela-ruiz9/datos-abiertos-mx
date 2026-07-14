# SEP — Estadísticas del Sistema Educativo Nacional

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Secretaría de Educación Pública |
| **Sector** | educación |
| **Periodicidad** | anual (inicio de ciclo escolar) |
| **Última actualización** | presente |
| **Formato** | Excel, CSV |
| **Licencia** | uso libre |
| **Cobertura geográfica** | nacional / estatal / municipal / plantel |
| **Cobertura temporal** | 1990 — presente |

## Descripción

La SEP publica anualmente el Formato 911 con estadísticas completas del sistema educativo nacional. Cubre desde preescolar hasta posgrado, desagregado por entidad, municipio, tipo de sostenimiento (público/privado) y modalidad. Es la fuente de referencia para matrícula, infraestructura educativa y flujo escolar (abandono, eficiencia terminal).

## URL de acceso

- Portal estadísticas SEP: https://www.planeacion.sep.gob.mx/estadisticaeindicadores.aspx
- Principales Cifras (descarga): https://www.planeacion.sep.gob.mx/principalescifras/
- datos.gob.mx SEP: https://www.datos.gob.mx/organization/ (buscar "SEP")

## Variables principales

| Variable | Tipo | Descripción |
|----------|------|-------------|
| ciclo_escolar | STR | Ciclo educativo (ej. 2023-2024) |
| entidad | STR | Estado |
| nivel | STR | Preescolar / Primaria / Secundaria / Media Superior / Superior |
| sostenimiento | STR | Público / Privado |
| alumnos | INT | Matrícula total |
| docentes | INT | Total de docentes |
| escuelas | INT | Total de planteles |
| abandono_escolar | FLOAT | Tasa de abandono (%) |
| eficiencia_terminal | FLOAT | % de alumnos que concluyen el nivel |

## Ejemplo de uso (Python)

```python
import pandas as pd

# Descargar el archivo de Principales Cifras desde el portal SEP
# Formato: Excel con múltiples hojas por nivel educativo
df = pd.read_excel(
    "principales_cifras_2023_2024.xlsx",
    sheet_name="Primaria",
    header=4,
)
df = df.dropna(subset=["Entidad"])
df_pub = df[df["Sostenimiento"] == "Público"]
print(df_pub.groupby("Entidad")["Alumnos"].sum().sort_values(ascending=False))
```

## Notas de calidad

- Los Excels de la SEP tienen encabezados multinivel y filas de totales intercaladas — limpiar con cuidado antes de analizar
- Los ciclos escolares van de agosto a julio del año siguiente (ej. 2023-2024 = ago 2023 – jul 2024)
- Para datos a nivel de plantel, el Formato 911 tiene granularidad individual de escuela
- Los nombres de columnas cambian entre ciclos — revisar el archivo antes de usar nombres hardcodeados

## Referencias

- Metodología Formato 911: https://www.planeacion.sep.gob.mx/estadisticaeindicadores.aspx
- MEJOREDU (indicadores de calidad): https://www.gob.mx/mejoredu
