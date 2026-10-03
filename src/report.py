import os

import matplotlib.pyplot as plt


def create_product_chart(df):

    os.makedirs("output/charts", exist_ok=True)

    product_sales = (
        df.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    product_sales.plot(kind="bar")

    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales")

    plt.tight_layout()

    plt.savefig("output/charts/sales_by_product.png")

    plt.close()


def create_sales_report(kpis):

    os.makedirs("output/charts", exist_ok=True)

    with open(
        "output/reports/sales_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        
        file.write("COMPANY SALES ANALYTICS REPORT\n")
        file.write("=" * 40 + "\n\n")

        for key, value in kpis.items():

            if isinstance(value, float):
                file.write(f"{key}: ₹{value:,.2f}\n")
            else:
                file.write(f"{key}: {value}\n")