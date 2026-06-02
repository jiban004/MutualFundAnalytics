# Day 1 – Data Ingestion & Initial Data Quality Report

## Objective

The objective of Day 1 was to set up the project environment, ingest mutual fund datasets, validate data integrity, and understand the dataset structure for future analysis.

## Datasets Loaded

1. 01_fund_master.csv
2. 02_nav_history.csv
3. 03_aum_by_fund_house.csv
4. 04_monthly_sip_inflows.csv
5. 05_category_inflows.csv
6. 06_industry_folio_count.csv
7. 07_scheme_performance.csv
8. 08_investor_transactions.csv
9. 09_portfolio_holdings.csv
10. 10_benchmark_indices.csv

## Fund Master Analysis

The fund master dataset contains scheme-level metadata including:

* AMFI Code
* Fund House
* Scheme Name
* Category
* Sub Category
* Plan Type
* Benchmark
* Expense Ratio
* Exit Load
* Fund Manager
* Risk Category

The AMFI code acts as the unique identifier for each mutual fund scheme.

## NAV History Analysis

The NAV history dataset contains:

* AMFI Code
* NAV Date
* NAV Value

This dataset stores historical NAV records and can be linked to the fund master dataset through the AMFI code.

## Data Quality Checks Performed

### Missing Value Check

Missing values were analyzed across the datasets using Pandas.

### Duplicate Record Check

Duplicate records were checked and identified using the duplicated() function.

### AMFI Code Validation

AMFI codes from the fund master dataset were compared against AMFI codes available in the NAV history dataset to ensure referential integrity.

## Key Observations

* All datasets were successfully loaded into Pandas.
* Dataset structures and column types were reviewed.
* AMFI codes provide a reliable link between scheme metadata and NAV history.
* Initial data quality validation was completed.
* The datasets are ready for preprocessing and analytical transformations.

## Deliverables Completed

* Project folder structure created
* Git repository initialized
* Dependencies installed
* Requirements file generated
* Data ingestion script created
* Live NAV ingestion script created
* Dataset exploration completed
* Data quality checks completed

### Data Quality Findings

* No duplicate records were found in the Fund Master dataset.
* No duplicate records were found in the NAV History dataset.
* AMFI code validation was successfully completed.
* Fund Master and NAV History datasets can be linked using the AMFI code.
* Dataset integrity appears good for further analysis and ETL processing.

## Conclusion

Day 1 objectives were successfully completed. The project environment is ready for ETL processing, data transformation, exploratory analysis, and dashboard development in subsequent phases.
