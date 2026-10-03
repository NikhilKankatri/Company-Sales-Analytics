from src.analysis import calculate_kpis, sales_by_customer, sales_by_product
from src.cleaner import clean_sales_data
from src.data_loader import load_sales_data
from src.database import connect_database, load_data_to_database
from src.excel_report import create_excel_report
from src.report import create_product_chart, create_sales_report
from src.transformations import calculate_sales, create_sales_category
from src.validator import validate_columns, validate_values

FILE_PATH = "data/raw/daily_sales.csv"


def main():

    print("=" * 50)
    print("COMPANY SALES & OPERATIONS ANALYTICS")
    print("=" * 50)

    # 1. Load data
    df = load_sales_data(FILE_PATH)

    if df is None:
        return

    # 2. Validate structure
    if not validate_columns(df):
        return

    # 3. Check data quality
    issues = validate_values(df)

    print("\nData Quality Check")
    print("------------------")

    for issue, count in issues.items():
        print(f"{issue}: {count}")

    # 4. Clean data
    df = clean_sales_data(df)

    print(f"\nClean records: {len(df)}")

    # 5. Calculate sales
    df = calculate_sales(df)

    # 6. Create business categories
    df = create_sales_category(df)

    # 7. Calculate KPIs
    kpis = calculate_kpis(df)

    print("\nBusiness KPIs")
    print("-------------")

    for key, value in kpis.items():
        print(f"{key}: {value:,.2f}")

    # 8. Product analysis
    print("\nSales by Product")
    print("----------------")

    print(sales_by_product(df))

    # 9. Customer analysis
    print("\nSales by Customer")
    print("-----------------")

    print(sales_by_customer(df))

    # 10. Save processed data
        # 10. Save processed data
    df.to_csv(
        "data/processed/cleaned_sales.csv",
        index=False
    )

    # 10.5 Load data into PostgreSQL
    connection = connect_database()

    if connection:
        load_data_to_database(df, connection)
        connection.close()

    # 11. Create chart
    create_product_chart(df)

    # 12. Create report
    create_sales_report(kpis)
    
    # 13. Create Excel report
    create_excel_report(df, kpis)

    print("\nProcessing completed successfully.")
    print("Processed data saved.")
    print("Chart generated.")
    print("Report generated.")


if __name__ == "__main__":
    main()