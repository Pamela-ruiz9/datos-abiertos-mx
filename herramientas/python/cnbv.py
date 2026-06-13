"""Utilidades para leer datos del Portafolio de Información de la CNBV."""

import pandas as pd
from pathlib import Path


def leer_tabla_banca_multiple(
    ruta: str | Path,
    encoding: str = "latin-1",
) -> pd.DataFrame:
    """
    Lee una tabla del boletín de Banca Múltiple de la CNBV.

    Los CSVs de la CNBV tienen:
    - Encoding Latin-1
    - Headers multinivel en filas 0-2
    - Comas como separador de miles

    Returns:
        DataFrame con headers aplanados (multinivel unido con "_")
    """
    df = pd.read_csv(
        ruta,
        encoding=encoding,
        header=[0, 1, 2],
        thousands=",",
    )
    df.columns = [
        "_".join(str(c) for c in col if "Unnamed" not in str(c)).strip()
        for col in df.columns
    ]
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]
    return df
