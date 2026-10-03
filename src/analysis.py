def calculate_kpis(df):

    total_sales = df["Sales"].sum()
    total_orders = df["Order_ID"].nunique()
    total_quantity = df["Quantity"].sum()
    average_order_value = total_sales / total_orders

    return {
        "Total Sales": total_sales,
        "Total Orders": total_orders,
        "Total Quantity": total_quantity,
        "Average Order Value": average_order_value
    }


def sales_by_product(df):

    return (
        df.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


def sales_by_customer(df):

    return (
        df.groupby("Customer")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )