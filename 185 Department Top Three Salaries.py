import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    def whichTop3(data):
        ind = sorted(list(set(data)), reverse=True)[:3]
        return [x in ind for x in data]
    if len(employee.index) == 0:
        return pd.DataFrame({"Department": [], "Employee": [], "Salary": []})
    ret = (employee.
        join(department.set_index('id').rename(columns={"name": "Department"}), on="departmentId").
        groupby("Department").
        apply(lambda x: x.loc[whichTop3(x["salary"]), ["salary", "name", "Department"]]).
        rename({"name": "Employee", "salary": "Salary"}, axis=1)[[
            "Department", "Employee", "Salary"
        ]])
    return ret
