import os

import psycopg2


def connect_database():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="sales_analysis",
            user="postgres",
            password=os.getenv("POSTGRES_PASSWORD"),
            port="5432"
        )

        print("PostgreSQL connected successfully.")

        return connection

    except Exception as error:
        print("Database connection failed.")
        print(error)

        return None


def load_data_to_database(df, connection):

    cursor = connection.cursor()

    try:
        for _, row in df.iterrows():

            cursor.execute(
                """
                INSERT INTO company_sales
                (order_id, customer, product, quantity, price, sales, sales_category)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (order_id)
                DO UPDATE SET
                    customer = EXCLUDED.customer,
                    product = EXCLUDED.product,
                    quantity = EXCLUDED.quantity,
                    price = EXCLUDED.price,
                    sales = EXCLUDED.sales,
                    sales_category = EXCLUDED.sales_category
                """,
                (
                    row["Order_ID"],
                    row["Customer"],
                    row["Product"],
                    int(row["Quantity"]),
                    row["Price"],
                    row["Sales"],
                    row["Sales_Category"]
                )
            )

        connection.commit()

        print("Data loaded into PostgreSQL successfully.")

    except Exception as error:

        connection.rollback()

        print("Error loading data:")
        print(error)

    finally:

        cursor.close()