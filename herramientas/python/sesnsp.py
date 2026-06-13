"""Utilidades para leer y limpiar datos del SESNSP."""

import pandas as pd
from pathlib import Path


def leer_incidencia(ruta: str | Path, encoding: str = "latin-1") -> pd.DataFrame:
    """
    Lee un CSV de incidencia delictiva del SESNSP.

    El SESNSP publica archivos con nombres como IDEFC_NM_abr24.csv.
    Las columnas de meses (enero-diciembre) son conteos de carpetas.

    Returns:
        DataFrame con columnas estandarizadas en minúsculas
    """
    df = pd.read_csv(ruta, encoding=encoding, low_memory=False)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df


def homicidios_por_estado(df: pd.DataFrame, año: int) -> pd.Series:
    """Suma de homicidios dolosos por estado para el año indicado."""
    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
    ]
    mask = (
        (df["tipo_de_delito"] == "Homicidio") &
        (df["modalidad"] == "Doloso") &
        (df["año"] == año)
    )
    return (
        df[mask]
        .groupby("entidad")[meses]
        .sum()
        .sum(axis=1)
        .sort_values(ascending=False)
    )
