import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # person.drop(person[person["email"].duplicated()].index, inplace=True)
    # person.groupby("email").agg("min")
    person.sort_values("id", inplace=True)
    person.drop_duplicates("email", inplace=True)
    
