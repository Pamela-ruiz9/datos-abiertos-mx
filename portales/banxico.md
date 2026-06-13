# Banxico SIE — Sistema de Información Económica

## ¿Qué es?

El SIE de Banxico es la principal fuente de series macroeconómicas y financieras de México. Cubre tipo de cambio, tasas de interés, inflación, agregados monetarios, balanza de pagos, crédito bancario y estadísticas del sistema financiero. Tiene API REST bien documentada.

## ¿Qué datos tiene?

| Categoría | Series destacadas |
|-----------|-------------------|
| Tipo de cambio | FIX, interbancario 48 hrs, paridades |
| Tasas de interés | TIIE 28d, TIIE 91d, Cetes, fondeo |
| Inflación | INPC general, subyacente, no subyacente |
| Reservas | Reservas internacionales, activos |
| Agregados monetarios | M1, M2, M3, base monetaria |
| Crédito | Crédito bancario por sector |
| Balanza de pagos | Cuenta corriente, remesas, IED |

## Cómo acceder

Requiere **token gratuito**:
1. Solicitarlo en https://www.banxico.org.mx/SieAPIRest/service/v1/token
2. Se recibe por correo en 1-2 días hábiles
3. Usar en header HTTP: `Bmx-Token: tu_token`

**Límite:** 10,000 consultas/día por token.

**Catálogo de series:** https://www.banxico.org.mx/SieAPIRest/service/v1/doc/catalogoSeries

## Tip de navegación

Buscar el ID de una serie en el catálogo (formato `SF{número}` o `SP{número}` o `SG{número}`). Las series más usadas empiezan con `SF43` (tipo de cambio) y `SF61` (tasas).

```python
# Ver herramientas/python/banxico_sie.py para cliente reutilizable
from banxico_sie import get_oportuno, SERIES_COMUNES
```

## Limitaciones

- El token se obtiene con correo corporativo/institucional preferentemente (aunque acepta personales)
- Las series de fines de semana y días festivos pueden aparecer sin datos — usar endpoint `/datos/oportuno`
- Las series históricas pueden tener gaps o cambios metodológicos — revisar documentación de cada serie
- No hay sandbox — las consultas de prueba consumen el cupo de 10,000/día

## Fichas relacionadas en este catálogo

- Ver `catalogo/finanzas/banxico-sie.md` para documentación completa con series más usadas
