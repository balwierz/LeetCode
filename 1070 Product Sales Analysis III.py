import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    def getFirstYear(df):
        firstYear = df["year"].min()
        return df.loc[df.year == firstYear]
    return sales.drop('sale_id', axis=1).groupby("product_id").apply(getFirstYear).rename(columns={"year": "first_year"})
