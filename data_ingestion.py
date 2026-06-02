import pandas as pd
import os

DATA_PATH = "data/raw"

def load_and_profile_csv(file_path):
    df = pd.read_csv(file_path)

    print("\n" + "="*80)
    print(f"FILE: {os.path.basename(file_path)}")
    print("="*80)

    print("\nShape:", df.shape)

    print("\nColumns & Data Types:")
    print(df.dtypes)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    return df


def main():

    csv_files = sorted([
        f for f in os.listdir(DATA_PATH)
        if f.endswith(".csv")
    ])

    dataframes = {}

    for file in csv_files:
        path = os.path.join(DATA_PATH, file)
        df = load_and_profile_csv(path)
        dataframes[file] = df

    # -------------------------------
    # AMFI VALIDATION (Fund Master vs NAV)
    # -------------------------------

    fund_master = dataframes["01_fund_master.csv"]
    nav_history = dataframes["02_nav_history.csv"]

    master_codes = set(fund_master["amfi_code"])
    nav_codes = set(nav_history["amfi_code"])

    missing_codes = master_codes - nav_codes

    print("\n" + "="*80)
    print("AMFI VALIDATION SUMMARY")
    print("="*80)

    print("Total Fund Master Codes:", len(master_codes))
    print("Total NAV Codes:", len(nav_codes))
    print("Missing Codes:", len(missing_codes))

    print("\nSample Missing Codes:", list(missing_codes)[:10])


if __name__ == "__main__":
    main()