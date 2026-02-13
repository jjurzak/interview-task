import pandas as pd
import re


fruit_sales = pd.DataFrame(
    {"quantity": [10, 3], "price": [10, 1]}, index=["banana", "apple"]
)
print(fruit_sales)


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    pattern = r"^[A-Za-z_]+$"

    if not re.match(pattern, new_column):
        return pd.DataFrame()

    for col in df.columns:
        if not re.match(pattern, col):
            return pd.DataFrame()

    df = df.copy()

    try:
        df[new_column] = df.eval(role)
    except Exception:
        return pd.DataFrame()

    return df


sales_total = add_virtual_column(fruit_sales, "quantity * price", "total")
print(sales_total)
