import pandas as pd
import re


fruit_sales = pd.DataFrame(
    {"quantity": [10, 3], "price": [10, 1]}, index=["banana", "apple"]
)


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


def operations(df: pd.DataFrame, operator: str) -> pd.DataFrame:
    expression = f"quantity {operator} price"
    return add_virtual_column(df, expression, "total")


print(operations(fruit_sales, "+"))
print(operations(fruit_sales, "-"))
print(operations(fruit_sales, "*"))
print(operations(fruit_sales, "dummy_errorr"))
