import pandas as pd
import numpy as np

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    a = ~insurance.duplicated(subset=["lat", "lon"], keep=False)
    b = insurance.duplicated(["tiv_2015"], keep=False)
    ret = insurance[a & b][["tiv_2016"]].sum()
    return pd.DataFrame({"tiv_2016": ret})
