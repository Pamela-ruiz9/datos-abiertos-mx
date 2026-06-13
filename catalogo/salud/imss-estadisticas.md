# IMSS — Estadísticas de Trabajadores Asegurados

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Instituto Mexicano del Seguro Social |
| **Sector** | salud / empleo |
| **Periodicidad** | mensual |
| **Última actualización** | presente |
| **Formato** | CSV |
| **Licencia** | uso libre |
| **Cobertura geográfica** | nacional / estatal |
| **Cobertura temporal** | 2000 — presente |

## Descripción

El IMSS publica mensualmente el número de trabajadores asegurados desagregado por entidad, delegación, tipo de empleo (permanente/eventual) y salario base de cotización. Es el principal indicador de empleo formal en México y se usa como indicador líder del mercado laboral.

## URL de acceso

- Portal estadísticas IMSS: https://www.imss.gob.mx/estadisticas
- Dataset trabajadores asegurados (datos.gob.mx): https://datos.gob.mx/busca/dataset/trabajadores-asegurados-al-imss
- Memoria estadística: https://www.imss.gob.mx/conoce-al-imss/memoria-estadistica

## Variables principales

| Variable | Tipo | Descripción |
|----------|------|-------------|
| fecha | DATE | Mes y año del reporte |
| entidad_federativa | STR | Estado |
| delegacion | STR | Delegación o subdelegación IMSS |
| trabajadores_asegurados | INT | Total asegurados en el periodo |
| trabajadores_permanentes | INT | Empleados con contrato permanente |
| trabajadores_eventuales_urbanos | INT | Eventuales en zona urbana |
| trabajadores_eventuales_campo | INT | Eventuales en actividad rural |
| salario_base_cotizacion | FLOAT | SBC promedio (pesos/día) |

## Ejemplo de uso (Python)

```python
import pandas as pd

# Patrón de URL de archivos IMSS en datos.gob.mx
# Verificar URL actualizada en https://datos.gob.mx/busca/dataset/trabajadores-asegurados-al-imss
url = "https://datos.imss.gob.mx/sites/default/files/asg-2024-03-01.csv"

df = pd.read_csv(url, encoding="latin-1")
df["fecha"] = pd.to_datetime(df["fecha"])

nacional = df.groupby("fecha")["trabajadores_asegurados"].sum()
print(nacional.tail(12))
```

## Notas de calidad

- Los archivos CSV usan encoding **Latin-1**
- El patrón de URL cambia con cada actualización — verificar el enlace vigente en datos.gob.mx
- El IMSS solo cubre empleo **formal** — para empleo total (formal + informal) usar INEGI ENOE (`catalogo/economia/enoe-empleo.md`)
- El salario base de cotización (SBC) es el salario reportado al IMSS, puede diferir del salario real

## Referencias

- Metodología: https://www.imss.gob.mx/estadisticas
- ENOE para empleo total: https://www.inegi.org.mx/programas/enoe/15ymas/
