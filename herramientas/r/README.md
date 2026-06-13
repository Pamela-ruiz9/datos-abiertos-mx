# Herramientas R

Clientes para acceder a las principales APIs de datos abiertos de México desde R.

## Dependencias

```r
install.packages(c("httr", "jsonlite", "tidyverse"))
```

## Módulos disponibles

| Archivo | Fuente | Requiere token |
|---------|--------|---------------|
| `banxico_sie.R` | Banxico SIE | Sí |
| `inegi_bie.R` | INEGI BIE | Sí |

## Variables de entorno

```r
Sys.setenv(BANXICO_TOKEN = "tu_token")
Sys.setenv(INEGI_TOKEN   = "tu_token")
```

## Uso rápido

```r
source("banxico_sie.R")
token <- Sys.getenv("BANXICO_TOKEN")

# Tipo de cambio FIX más reciente
fix <- get_oportuno(SERIES_COMUNES$fix, token)
cat("FIX:", fix$fecha, "-", fix$dato, "MXN/USD\n")

# Últimos 8 trimestres de desocupación
source("inegi_bie.R")
token_inegi <- Sys.getenv("INEGI_TOKEN")
df <- get_indicador(INDICADORES_COMUNES$desocupacion, token_inegi)
tail(df, 8)
```
