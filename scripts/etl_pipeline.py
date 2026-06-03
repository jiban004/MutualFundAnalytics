import pandas as pd
import os
from pathlib import Path

RAW_PATH = Path("data/raw")
PROCESSED_PATH = Path("data/processed")

def load_csv(file_name):
    path = RAW_PATH / file_name
    df = pd.read_csv(path)

    print(f"\nLoaded: {file_name}")
    print("Shape:", df.shape)

    # basic checks
    print("Missing values:\n", df.isnull().sum())
    print("Duplicates:", df.duplicated().sum())

    return df


def main():

    print("\n========== ETL PIPELINE STARTED ==========\n")

    datasets = {
        "fund_master": "01_fund_master.csv",
        "nav_history": "02_nav_history.csv",
        "aum": "03_aum_by_fund_house.csv",
        "sip": "04_monthly_sip_inflows.csv",
        "category_inflows": "05_category_inflows.csv",
        "industry_folio": "06_industry_folio_count.csv",
        "scheme_perf": "07_scheme_performance.csv",
        "transactions": "08_investor_transactions.csv",
        "holdings": "09_portfolio_holdings.csv",
        "benchmark": "10_benchmark_indices.csv"
    }

    dataframes = {}

    for name, file in datasets.items():
        dataframes[name] = load_csv(file)

    # AMFI validation
    print("\n========== AMFI VALIDATION ==========\n")

    master = dataframes["fund_master"]
    nav = dataframes["nav_history"]

    master_codes = set(master["amfi_code"])
    nav_codes = set(nav["amfi_code"])

    missing = master_codes - nav_codes

    print("Total Fund Master Codes:", len(master_codes))
    print("Total NAV Codes:", len(nav_codes))
    print("Missing Codes:", len(missing))

    print("\nSample Missing Codes:", list(missing)[:10])

    print("\n========== ETL COMPLETED ==========\n")


if __name__ == "__main__":
    main()