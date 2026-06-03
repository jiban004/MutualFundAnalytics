import pandas as pd
import sqlite3
from pathlib import Path

DATA_PATH = Path("data/raw")
DB_PATH = Path("data/db/bluestock_mf.db")

conn = sqlite3.connect(DB_PATH)

def load_csv_to_sql(file_name, table_name):
    df = pd.read_csv(DATA_PATH / file_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {file_name} → {table_name}")

def main():

    # Core tables
    load_csv_to_sql("01_fund_master.csv", "fund_master")
    load_csv_to_sql("02_nav_history.csv", "nav_history")
    load_csv_to_sql("03_aum_by_fund_house.csv", "aum_by_fund_house")
    load_csv_to_sql("04_monthly_sip_inflows.csv", "monthly_sip_inflows")
    load_csv_to_sql("05_category_inflows.csv", "category_inflows")
    load_csv_to_sql("06_industry_folio_count.csv", "industry_folio_count")
    load_csv_to_sql("07_scheme_performance.csv", "scheme_performance")
    load_csv_to_sql("08_investor_transactions.csv", "investor_transactions")
    load_csv_to_sql("09_portfolio_holdings.csv", "portfolio_holdings")
    load_csv_to_sql("10_benchmark_indices.csv", "benchmark_indices")

    conn.commit()
    conn.close()

    print("\nDatabase created successfully!")

if __name__ == "__main__":
    main()