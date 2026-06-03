import pandas as pd
import numpy as np

# ---------------------------
# CAGR
# ---------------------------
def calculate_cagr(nav_df):

    results = []

    nav_df["date"] = pd.to_datetime(nav_df["date"])

    for code in nav_df["amfi_code"].unique():

        temp = nav_df[nav_df["amfi_code"] == code].sort_values("date")

        if len(temp) < 2:
            continue

        start = temp["nav"].iloc[0]
        end = temp["nav"].iloc[-1]

        days = (temp["date"].iloc[-1] - temp["date"].iloc[0]).days
        years = days / 365

        if start > 0 and years > 0:
            cagr = (end / start) ** (1 / years) - 1
            results.append([code, cagr])

    return pd.DataFrame(results, columns=["amfi_code", "CAGR"])


# ---------------------------
# Sharpe Ratio
# ---------------------------
def calculate_sharpe(nav_df):

    nav_df = nav_df.copy()
    nav_df["return"] = nav_df.groupby("amfi_code")["nav"].pct_change()

    results = []

    for code in nav_df["amfi_code"].unique():

        temp = nav_df[nav_df["amfi_code"] == code]

        mean_ret = temp["return"].mean()
        std_ret = temp["return"].std()

        if std_ret and std_ret != 0:
            sharpe = (mean_ret / std_ret) * np.sqrt(252)
            results.append([code, sharpe])

    return pd.DataFrame(results, columns=["amfi_code", "Sharpe"])


# ---------------------------
# VaR (95%)
# ---------------------------
def calculate_var(nav_df):

    nav_df = nav_df.copy()
    nav_df["return"] = nav_df.groupby("amfi_code")["nav"].pct_change()

    var_95 = np.percentile(nav_df["return"].dropna(), 5)

    return var_95


# ---------------------------
# Example Runner
# ---------------------------
if __name__ == "__main__":

    nav = pd.read_csv("../data/raw/02_nav_history.csv")

    cagr_df = calculate_cagr(nav)
    sharpe_df = calculate_sharpe(nav)
    var_value = calculate_var(nav)

    print("\nCAGR Sample:\n", cagr_df.head())
    print("\nSharpe Sample:\n", sharpe_df.head())
    print("\nVaR (95%):", var_value)