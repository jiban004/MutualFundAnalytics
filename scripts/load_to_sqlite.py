import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

# -----------------------------
# Paths
# -----------------------------
DATA_PATH = Path("data/processed")
DB_PATH = Path("data/db/bluestock_mf.db")

# -----------------------------
# SQLite Engine
# -----------------------------
engine = create_engine(f"sqlite:///{DB_PATH}")

# -----------------------------
# Files to load
# -----------------------------
tables = {
    "nav_history": "02_nav_history_cleaned.csv",
    "scheme_performance": "07_scheme_performance_cleaned.csv",
    "investor_transactions": "08_investor_transactions_cleaned.csv"
}

# -----------------------------
# Load Data
# -----------------------------
for table_name, file_name in tables.items():

    file_path = DATA_PATH / file_name

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"Loaded {table_name} "
        f"({len(df)} rows)"
    )

print("\nDatabase loading complete.")