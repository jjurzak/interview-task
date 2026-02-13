import pandas as pd


fruit_sales = pd.DataFrame({"quantity": [10, 3], "price": [10, 1]}, index=["banana", "apple"])
print(fruit_sales)

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    df = df.copy()
    df[new_column] = df.eval(role)
    return df


sales_total = add_virtual_column(fruit_sales, "quantity * price", "total")
print(sales_total)
