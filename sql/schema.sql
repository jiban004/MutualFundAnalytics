-- Fund Master Table
CREATE TABLE IF NOT EXISTS fund_master (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date TEXT,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount REAL,
    min_lumpsum_amount REAL,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT
);

-- NAV History Table
CREATE TABLE IF NOT EXISTS nav_history (
    amfi_code INTEGER,
    date TEXT,
    nav REAL,
    PRIMARY KEY (amfi_code, date)
);

-- AUM Table
CREATE TABLE IF NOT EXISTS aum_by_fund_house (
    fund_house TEXT,
    date TEXT,
    aum_cr REAL
);

-- SIP Inflows
CREATE TABLE IF NOT EXISTS monthly_sip_inflows (
    fund_house TEXT,
    month TEXT,
    inflow_cr REAL
);

-- Category Inflows
CREATE TABLE IF NOT EXISTS category_inflows (
    category TEXT,
    month TEXT,
    inflow_cr REAL
);