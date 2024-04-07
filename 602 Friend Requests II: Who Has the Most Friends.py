import pandas as pd

def most_friends(r: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(Counter(pd.concat([r.requester_id, r.accepter_id])).most_common(1), columns=["id", "num"])
