import pandas as pd

def find_employees(e: pd.DataFrame) -> pd.DataFrame:
    all_employees = set(e["employee_id"].values)
    return e.loc[(e["salary"] < 30_000) & \
        (~e["manager_id"].isin(all_employees) & \
        ~e["manager_id"].isna()
        ), ["employee_id"]].sort_values("employee_id")
