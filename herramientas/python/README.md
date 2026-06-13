# Herramientas Python

Clientes y utilidades para acceder a las principales APIs y fuentes de datos abiertos de México.

## Dependencias

```bash
pip install requests pandas openpyxl
# Para SEMARNAT/GIS:
pip install geopandas
```

## Módulos disponibles

| Archivo | Fuente | Requiere token |
|---------|--------|---------------|
| `banxico_sie.py` | Banxico SIE | Sí — banxico.org.mx/SieAPIRest |
| `inegi_bie.py` | INEGI BIE | Sí — inegi.org.mx/app/developer |
| `sesnsp.py` | SESNSP incidencia delictiva | No |
| `cnbv.py` | CNBV Portafolio de Información | No |

## Variables de entorno

```bash
export BANXICO_TOKEN="tu_token_banxico"
export INEGI_TOKEN="tu_token_inegi"
```

## Uso rápido

```python
# Tipo de cambio FIX más reciente
from banxico_sie import get_oportuno, SERIES_COMUNES
import os
dato = get_oportuno(SERIES_COMUNES["fix"], os.environ["BANXICO_TOKEN"])
print(dato)  # {'fecha': '2024-03-15', 'dato': '16.8234'}

# Tasa de desocupación — últimos 8 trimestres
from inegi_bie import get_indicador, INDICADORES_COMUNES
obs = get_indicador(
    INDICADORES_COMUNES["desocupacion"],
    os.environ["INEGI_TOKEN"],
    recientes=8,
)
for o in obs:
    print(o["TIME_PERIOD"], o["OBS_VALUE"])
```
