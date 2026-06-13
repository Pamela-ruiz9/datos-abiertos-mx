# Cliente para la API SIE de Banxico
# Dependencias: httr, jsonlite
# install.packages(c("httr", "jsonlite"))

library(httr)
library(jsonlite)

BANXICO_BASE <- "https://www.banxico.org.mx/SieAPIRest/service/v1"

SERIES_COMUNES <- list(
  fix            = "SF43718",
  tiie_28        = "SF61745",
  inpc           = "SP68257",
  reservas       = "SF46410",
  base_monetaria = "SG185"
)

#' Consulta una serie del SIE de Banxico
#'
#' @param serie Clave de la serie (ej. "SF43718")
#' @param token Token Banxico
#' @param desde Fecha inicio "YYYY-MM-DD" (opcional)
#' @param hasta Fecha fin "YYYY-MM-DD" (opcional)
#' @return data.frame con columnas fecha y dato
get_serie <- function(serie, token, desde = NULL, hasta = NULL) {
  if (!is.null(desde) && !is.null(hasta)) {
    url <- paste0(BANXICO_BASE, "/series/", serie, "/datos/", desde, "/", hasta)
  } else {
    url <- paste0(BANXICO_BASE, "/series/", serie, "/datos")
  }
  resp <- GET(url, add_headers("Bmx-Token" = token))
  stop_for_status(resp)
  datos <- content(resp, as = "parsed")$bmx$series[[1]]$datos
  do.call(rbind, lapply(datos, as.data.frame))
}

#' Retorna el valor más reciente de una serie
#' @param serie Clave de la serie
#' @param token Token Banxico
#' @return Lista con fecha y dato
get_oportuno <- function(serie, token) {
  url <- paste0(BANXICO_BASE, "/series/", serie, "/datos/oportuno")
  resp <- GET(url, add_headers("Bmx-Token" = token))
  stop_for_status(resp)
  content(resp, as = "parsed")$bmx$series[[1]]$datos[[1]]
}

# Ejemplo de uso:
# token <- Sys.getenv("BANXICO_TOKEN")
# fix <- get_oportuno(SERIES_COMUNES$fix, token)
# cat("FIX:", fix$fecha, "-", fix$dato, "MXN/USD\n")
