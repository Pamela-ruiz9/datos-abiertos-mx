"""Cliente para la API SIE de Banxico."""

import requests
from typing import Optional

BANXICO_BASE = "https://www.banxico.org.mx/SieAPIRest/service/v1"

SERIES_COMUNES = {
    "fix": "SF43718",
    "tiie_28": "SF61745",
    "inpc": "SP68257",
    "reservas": "SF46410",
    "base_monetaria": "SG185",
}


def get_serie(
    serie: str,
    token: str,
    desde: Optional[str] = None,
    hasta: Optional[str] = None,
) -> list[dict]:
    """
    Consulta una serie del SIE de Banxico.

    Args:
        serie: Clave de la serie (ej. "SF43718")
        token: Token Banxico — obtener en banxico.org.mx/SieAPIRest/service/v1/token
        desde: Fecha inicio "YYYY-MM-DD" (opcional)
        hasta: Fecha fin "YYYY-MM-DD" (opcional)

    Returns:
        Lista de dicts con claves "fecha" y "dato"
    """
    if desde and hasta:
        endpoint = f"{BANXICO_BASE}/series/{serie}/datos/{desde}/{hasta}"
    else:
        endpoint = f"{BANXICO_BASE}/series/{serie}/datos"

    r = requests.get(endpoint, headers={"Bmx-Token": token}, timeout=30)
    r.raise_for_status()
    return r.json()["bmx"]["series"][0]["datos"]


def get_oportuno(serie: str, token: str) -> dict:
    """Retorna el valor más reciente de una serie."""
    url = f"{BANXICO_BASE}/series/{serie}/datos/oportuno"
    r = requests.get(url, headers={"Bmx-Token": token}, timeout=30)
    r.raise_for_status()
    return r.json()["bmx"]["series"][0]["datos"][0]


def get_multiseries(series: list[str], token: str) -> dict[str, list[dict]]:
    """Descarga múltiples series en una sola llamada (hasta 20 series)."""
    claves = ",".join(series)
    url = f"{BANXICO_BASE}/series/{claves}/datos"
    r = requests.get(url, headers={"Bmx-Token": token}, timeout=30)
    r.raise_for_status()
    return {
        s["idSerie"]: s["datos"]
        for s in r.json()["bmx"]["series"]
    }


if __name__ == "__main__":
    import os

    TOKEN = os.environ.get("BANXICO_TOKEN", "")
    if not TOKEN:
        raise SystemExit("Exporta tu token: export BANXICO_TOKEN=tu_token")

    dato = get_oportuno(SERIES_COMUNES["fix"], TOKEN)
    print(f"Tipo de cambio FIX: {dato['fecha']} — {dato['dato']} MXN/USD")
