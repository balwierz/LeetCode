import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({"class": [x for x, c in Counter(courses["class"]).items() if c >= 5]})
