import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    toExclude = set(bonus[bonus.bonus >= 1000]["empId"])
    return employee[~employee.empId.isin(toExclude)].set_index("empId").join(bonus.set_index("empId"))[["name", "bonus"]]
