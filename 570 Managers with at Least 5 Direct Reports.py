import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    if not len(employee):
        return pd.DataFrame({"name": []})
    data = employee.groupby("managerId").apply(lambda x: len(x) >= 5).reset_index()
    data = data.loc[data[0]]
    return employee[["id", "name"]].set_index("id").join(data[["managerId"]].set_index("managerId"), how="inner")[["name"]]
