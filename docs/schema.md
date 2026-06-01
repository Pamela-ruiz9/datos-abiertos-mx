# Esquema de Ficha de Fuente

Cada fuente de datos se documenta con este esquema estándar en Markdown.

```markdown
# [Nombre de la fuente]

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | Nombre del organismo |
| **Sector** | economia / finanzas / salud / educacion / ... |
| **Periodicidad** | diaria / mensual / trimestral / anual / irregular |
| **Última actualización** | YYYY-MM |
| **Formato** | CSV / JSON / API REST / Excel / XML |
| **Licencia** | abierta / uso libre / condicionada |
| **Cobertura geográfica** | nacional / estatal / municipal |
| **Cobertura temporal** | año inicio — año fin (o "presente") |

## Descripción

Qué contiene esta fuente, qué mide, para qué sirve.

## URL de acceso

- Portal principal: https://...
- API endpoint: https://...
- Descarga directa: https://...

## Variables principales

| Variable | Tipo | Descripción |
|----------|------|-------------|
| fecha | DATE | Fecha de observación |
| ... | ... | ... |

## Ejemplo de uso (Python)

```python
import requests
# snippet básico para acceder a la fuente
```

## Notas de calidad

- Advertencias sobre datos faltantes, discontinuidades, cambios metodológicos
- Limitaciones conocidas
- Fuentes alternativas si esta falla

## Referencias

- Metodología oficial: https://...
- Documentación API: https://...
```
