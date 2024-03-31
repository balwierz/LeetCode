import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    def whichMax(data):
        m = max(data)
        return [x == m for x in data]
    if len(employee.index) == 0:
        return pd.DataFrame({"Department": [], "Employee": [], "Salary": []})
    ret = (employee.
        join(department.set_index('id').rename(columns={"name": "Department"}), on="departmentId").
        groupby("Department").
        apply(lambda x: x.loc[whichMax(x["salary"]), ["salary", "name", "Department"]]).
        rename({"name": "Employee", "salary": "Salary"}, axis=1))
    return ret
