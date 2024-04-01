import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    ret = person.join(address.set_index("personId"), on="personId")
    return ret[["firstName", "lastName", "city", "state"]]
