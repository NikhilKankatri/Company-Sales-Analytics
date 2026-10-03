import pandas as pd


def clean_sales_data(df):

    df = df.copy()

    # Convert Quantity and Price to numeric
    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    )

    df["Price"] = pd.to_numeric(
        df["Price"],
        errors="coerce"
    )

    # Remove rows with invalid quantity or price
    df = df[
        (df["Quantity"] > 0) &
        (df["Price"] > 0)
    ]

    # Remove duplicate orders
    df = df.drop_duplicates(subset="Order_ID")

    # Remove rows with missing important information
    df = df.dropna(
        subset=[
            "Order_ID",
            "Customer",
            "Product",
            "Quantity",
            "Price"
        ]
    )

    return df