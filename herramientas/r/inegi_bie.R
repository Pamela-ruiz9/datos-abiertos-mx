# Cliente para el BIE de INEGI
# Dependencias: httr, jsonlite
# install.packages(c("httr", "jsonlite"))

library(httr)
library(jsonlite)

INEGI_BIE_BASE <- paste0(
  "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml"
)

INDICADORES_COMUNES <- list(
  desocupacion = "444612",
  pib          = "216064",
  inpc         = "628229",
  subocupacion = "444637",
  informalidad = "444656"
)

#' Consulta un indicador del BIE de INEGI
#'
#' @param indicador ID del indicador (ej. "444612")
#' @param token Token INEGI — obtener en inegi.org.mx/app/developer/
#' @param area Clave geográfica (default "0700" = nacional)
#' @return data.frame con TIME_PERIOD y OBS_VALUE
get_indicador <- function(indicador, token, area = "0700") {
  url <- paste0(
    INEGI_BIE_BASE,
    "/INDICATOR/", indicador,
    "/es/", area,
    "/false/BIE/2.0/", token,
    "?type=json"
  )
  resp <- GET(url)
  stop_for_status(resp)
  obs <- content(resp, as = "parsed")$Series[[1]]$OBSERVATIONS
  do.call(rbind, lapply(obs, function(o) {
    data.frame(
      TIME_PERIOD = o$TIME_PERIOD,
      OBS_VALUE   = as.numeric(o$OBS_VALUE),
      stringsAsFactors = FALSE
    )
  }))
}

# Ejemplo de uso:
# token <- Sys.getenv("INEGI_TOKEN")
# df <- get_indicador(INDICADORES_COMUNES$desocupacion, token)
# tail(df, 8)
