# Company Sales & Operations Analytics

## Project Overview

A company-style sales analytics system built with Python, PostgreSQL, Pandas, NumPy, Matplotlib, Seaborn, and Excel automation.

The project simulates a real-world data analyst workflow:

**Raw Data → Validation → Cleaning → Transformation → Analysis → PostgreSQL → Reports → Visualization → Testing**

## Business Objective

The objective is to process raw sales data, identify data quality issues, calculate business KPIs, analyze products and customers, and generate automated reports for business decision-making.

## Key Features

* CSV data ingestion using Pandas
* Data validation and quality checks
* Handling invalid and missing values
* Duplicate order detection
* Sales calculation
* Sales value categorization
* Business KPI calculation
* Product and customer analysis
* PostgreSQL database integration
* SQL business analysis
* Excel report automation
* Matplotlib and Seaborn visualizations
* Outlier detection using IQR
* Automated testing with Pytest
* Modular Python project structure

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* PostgreSQL
* SQL
* OpenPyXL
* Pytest
* Jupyter Notebook
* Git & GitHub

## Key Business KPIs

| KPI                 |     Result |
| ------------------- | ---------: |
| Total Sales         |   ₹250,500 |
| Total Orders        |          8 |
| Total Quantity      |         19 |
| Average Order Value | ₹31,312.50 |

## Project Workflow

1. Load raw sales data from CSV.
2. Validate the dataset structure.
3. Check data quality.
4. Clean invalid records.
5. Calculate sales values.
6. Categorize orders by sales value.
7. Calculate business KPIs.
8. Analyze sales by product and customer.
9. Load processed data into PostgreSQL.
10. Perform SQL-based business analysis.
11. Generate Excel reports.
12. Perform exploratory data analysis.
13. Create visualizations.
14. Detect potential outliers.
15. Run automated tests.

## Project Structure

```text
Company_Sales_Analytics
│
├── data
│   ├── raw
│   │   └── daily_sales.csv
│   ├── processed
│   │   └── cleaned_sales.csv
│   └── reference
│
├── src
│   ├── __init__.py
│   ├── data_loader.py
│   ├── validator.py
│   ├── cleaner.py
│   ├── transformations.py
│   ├── analysis.py
│   ├── report.py
│   ├── database.py
│   └── excel_report.py
│
├── notebooks
│   └── exploratory_analysis.ipynb
│
├── output
│   ├── charts
│   └── reports
│
├── tests
│   └── test_transformations.py
│
├── main.py
├── requirements.txt
└── README.md
```

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure PostgreSQL

Create a PostgreSQL database named:

```text
sales_analysis
```

Create the required `company_sales` table using the SQL provided in the project.

Update the PostgreSQL connection details in:

```text
src/database.py
```

### 3. Run the analytics pipeline

```bash
python main.py
```

The pipeline generates:

* Cleaned CSV data
* PostgreSQL records
* Sales charts
* Text report
* Excel report

## Outputs

### Excel Report

The automated Excel report contains:

* KPI Summary
* Sales Data
* Product Analysis
* Customer Analysis

### Visualizations

The project generates charts for:

* Sales by Product
* Sales by Customer
* Sales by Category
* Sales Distribution
* Quantity vs Sales
* Sales Outlier Detection
* Product Sales Contribution

## Testing

Run:

```bash
pytest
```

The test suite verifies important data transformation logic such as sales calculations.

## Business Insights

Based on the current sample dataset:

* Laptops generate the largest share of sales.
* Rahul is the highest-sales customer.
* Total sales are ₹250,500 across 8 orders.
* The average order value is ₹31,312.50.
* The dataset contains intentionally invalid records that are removed during the cleaning stage.

## Learning Outcomes

This project demonstrates practical experience with:

* Python programming
* File handling
* Data cleaning
* Data validation
* Pandas
* NumPy
* Data visualization
* Exploratory data analysis
* SQL
* PostgreSQL
* Excel automation
* Testing
* Modular programming
* Basic ETL workflow
* Business analytics

## Author

**Nikhil Kankatri**

B.E. Computer Science & Engineering
IoT, Cybersecurity and Blockchain
