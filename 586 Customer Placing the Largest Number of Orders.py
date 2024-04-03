import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    data = orders.groupby("customer_number").agg(lambda x: len(x))
    m = float(data.apply(max, default=0))
    return data[data["order_number"] == m].reset_index()[["customer_number"]]

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].mode().to_frame()
