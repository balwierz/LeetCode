import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    #weather.loc[weather["recordDate"]]
    yesterday = pd.DataFrame({"recordDate": weather["recordDate"] + datetime.timedelta(days=1),
        "temperature": weather["temperature"]})
    data = weather.join(yesterday.set_index("recordDate"), 
        on="recordDate", how="inner", lsuffix="_today", rsuffix="_yesterday")
    return data.loc[data.temperature_today > data.temperature_yesterday][["id"]]

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    return weather[(weather.temperature.diff() > 0) & (weather.recordDate.diff().dt.days == 1)][['id']]
