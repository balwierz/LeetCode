import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # first login
    firstLogin = activity.groupby("player_id")["event_date"].min().reset_index()
    firstLogin["event_date"] += datetime.timedelta(days=1)  # now it is the day after
    out = firstLogin.join(activity.set_index(["player_id", "event_date"]), how='inner', on=["player_id", "event_date"])
    return pd.DataFrame({"fraction": [round(len(out)/len(firstLogin), 2)]})
