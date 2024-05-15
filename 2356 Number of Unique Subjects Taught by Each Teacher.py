import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    #return teacher.groupby("teacher_id").agg({"subject_id": lambda x: len(set(x)) }).reset_index().rename(columns = {"subject_id": "cnt"})
    return teacher.groupby('teacher_id')['subject_id'].nunique().reset_index(name='cnt')
