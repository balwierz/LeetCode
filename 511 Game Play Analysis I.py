import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby("player_id")["event_date"].min().reset_index(name="first_login")
    return (activity[["player_id", "event_date"]]
        .groupby("player_id").apply(min)
        .rename({"event_date": "first_login"}, axis=1)
        )
