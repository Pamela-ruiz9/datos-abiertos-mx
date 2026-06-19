"""Cliente para el Banco de Información Económica (BIE) del INEGI."""

import requests
from typing import Optional

INEGI_BIE_BASE = (
    "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml"
)

INDICADORES_COMUNES = {
    "desocupacion": "444612",
    "pib": "216064",
    "inpc_variacion": "628229",
    "subocupacion": "444637",
    "informalidad": "444656",
}


def get_indicador(
    indicador: str,
    token: str,
    area: str = "0700",
    recientes: Optional[int] = None,
) -> list[dict]:
    """
    Consulta un indicador del BIE de INEGI.

    Args:
        indicador: ID del indicador (ej. "444612")
        token: Token INEGI — obtener en inegi.org.mx/app/developer/
        area: Clave geográfica (0700=nacional, 0101=Aguascalientes, etc.)
        recientes: Si se especifica, devuelve solo los N datos más recientes

    Returns:
        Lista de dicts con claves "TIME_PERIOD" y "OBS_VALUE"
    """
    url = (
        f"{INEGI_BIE_BASE}/INDICATOR/{indicador}/es/{area}"
        f"/false/BIE/2.0/{token}?type=json"
    )
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    body = r.json()
    if "ERROR" in body:
        raise ValueError(f"INEGI BIE error: {body['ERROR']}")
    obs = body["Series"][0]["OBSERVATIONS"]
    if recientes:
        return obs[-recientes:]
    return obs


def get_multiples(
    indicadores: dict[str, str],
    token: str,
    area: str = "0700",
) -> dict[str, list[dict]]:
    """
    Descarga múltiples indicadores.

    Args:
        indicadores: Dict nombre→id (ej. {"desocupacion": "444612"})
        token: Token INEGI
        area: Clave geográfica

    Returns:
        Dict nombre→lista de observaciones
    """
    return {
        nombre: get_indicador(id_, token, area)
        for nombre, id_ in indicadores.items()
    }


if __name__ == "__main__":
    import os

    TOKEN = os.environ.get("INEGI_TOKEN", "")
    if not TOKEN:
        raise SystemExit("Exporta tu token: export INEGI_TOKEN=tu_token")

    obs = get_indicador(INDICADORES_COMUNES["desocupacion"], TOKEN, recientes=8)
    print("Tasa de desocupación — últimos 8 trimestres:")
    for o in obs:
        print(f"  {o['TIME_PERIOD']}: {o['OBS_VALUE']}%")
