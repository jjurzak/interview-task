import pandas as pd
import re


fruit_sales = pd.DataFrame({"quantity": [10, 3], "price": [10, 1]}, index=["banana", "apple"])
print(fruit_sales)




def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    
    if not re.match(r'^[A-Za-z_]+$', new_column):
        raise ValueError("Col can only contain letter and underscore")

    df = df.copy()

    try:
        df[new_column] = df.eval(role)
    except Exception:
        return pd.DataFrame()

    return df


sales_total = add_virtual_column(fruit_sales, "quantity * price", "total")
print(sales_total)
