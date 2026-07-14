# SHCP — Transparencia Presupuestaria

## ¿Qué es?

El portal de Transparencia Presupuestaria de la SHCP es la fuente oficial del gasto público federal mexicano. Publica el Presupuesto de Egresos de la Federación (PEF) aprobado y ejercido a nivel de programa, dependencia y proyecto de inversión, actualizando mensualmente.

También administra la Cartera de Proyectos de Inversión para proyectos estratégicos mayores a 100 MDP.

## ¿Qué datos tiene?

| Módulo | Contenido |
|--------|-----------|
| PEF por dependencia | Gasto aprobado, modificado, devengado, ejercido |
| Cartera de inversión | Proyectos estratégicos, avances físicos y financieros |
| Cuenta Pública | Cierre del ejercicio fiscal anual |
| Ingresos presupuestarios | Recaudación vs meta LIF |
| Deuda pública | Saldo de deuda por instrumento |

## Cómo acceder

Sin registro. Descarga CSV directa o API REST:

```python
import requests
url = "https://www.transparenciapresupuestaria.gob.mx/ptp/contenido/api"
r = requests.get(url, params={"type": "egresos", "anio": 2024}, timeout=60)
```

Diccionario de parámetros: https://www.transparenciapresupuestaria.gob.mx/es/PTP/Datos_Abiertos

## Tip de navegación

Para comparar presupuesto aprobado vs ejercido por dependencia: ir a "Presupuesto" → "Gasto Programable" → exportar CSV.

## Limitaciones

- La estructura de parámetros de la API cambia entre ejercicios fiscales
- CSVs en encoding Latin-1 con comas como miles
- La Cartera solo cubre proyectos ≥ 100 MDP
- El gasto "devengado" de diciembre incluye compromisos no pagados — usar "ejercido" para análisis de flujo

## Fichas relacionadas en este catálogo

- Ver `catalogo/economia/shcp-transparencia-presupuestaria.md` para documentación completa
