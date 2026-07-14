# CONACYT/SECITI — Indicadores de Ciencia y Tecnología

## Metadata

| Campo | Valor |
|-------|-------|
| **Institución** | CONAHCYT (antes CONACYT; actualmente SECITI) + INEGI (ESIDET) |
| **Sector** | ciencia y tecnología |
| **Periodicidad** | bienal (ESIDET); anual (indicadores CONAHCYT) |
| **Última actualización** | 2022 |
| **Formato** | Excel, CSV |
| **Licencia** | uso libre |
| **Cobertura geográfica** | nacional / estatal / sector |
| **Cobertura temporal** | 2000 — presente |

## Descripción

Los indicadores de ciencia y tecnología de México se publican principalmente a través de dos fuentes: la Encuesta sobre Investigación y Desarrollo Experimental (ESIDET) del INEGI, y las publicaciones anuales del CONAHCYT (antes CONACYT, actualmente en transición a SECITI). Cubren gasto en I+D, personal investigador, patentes y producción científica.

## URL de acceso

- INEGI ESIDET: https://www.inegi.org.mx/programas/esidet/
- CONAHCYT indicadores: https://conahcyt.mx/
- datos.gob.mx ciencia: https://www.datos.gob.mx/dataset/ (buscar "ciencia y tecnología")
- OCDE estadísticas México: https://www.oecd.org/sti/msti2023.htm

## Variables principales

| Variable | Tipo | Descripción |
|----------|------|-------------|
| año | INT | Año de referencia |
| sector | STR | Gobierno / Educación Superior / Empresas / Privado sin fines de lucro |
| GIDE | FLOAT | Gasto en I+D (millones de pesos corrientes) |
| GIDE_pct_PIB | FLOAT | GIDE como % del PIB |
| investigadores_ETC | INT | Investigadores equivalentes a tiempo completo |
| patentes_solicitadas | INT | Patentes solicitadas en el IMPI |
| patentes_otorgadas | INT | Patentes otorgadas |
| publicaciones_WoS | INT | Publicaciones indexadas en Web of Science |

## Ejemplo de uso (Python)

```python
import pandas as pd

# Descargar desde datos.gob.mx o INEGI ESIDET
df = pd.read_excel("esidet_2021.xlsx", sheet_name="GIDE_sector", header=3)
df = df.dropna(subset=["año"])

# Gasto en I+D como % del PIB por año
gide_pib = df.groupby("año")["GIDE_pct_PIB"].mean()
print(gide_pib)
```

## Notas de calidad

- México invierte consistentemente ~0.3% del PIB en I+D (muy por debajo del promedio OCDE de 2.7%)
- El cambio institucional CONACYT → CONAHCYT → SECITI (2022-2025) genera inconsistencias en series históricas
- La ESIDET es bienal — hay años sin datos; interpolar con precaución
- Para comparaciones internacionales, usar datos OCDE que armoniza las cifras mexicanas con el estándar Frascati
- Las patentes IMPI no equivalen a patentes internacionales (USPTO/EPO) — son distintas jurisdicciones

## Referencias

- Metodología ESIDET: https://www.inegi.org.mx/programas/esidet/
- Informe general CONAHCYT: https://conahcyt.mx/
- OCDE MSTI (comparativa internacional): https://www.oecd.org/sti/msti2023.htm
- IMPI (patentes): https://datosabiertos.impi.gob.mx/Paginas/Inicio.aspx
