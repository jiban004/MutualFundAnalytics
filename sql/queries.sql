SELECT COUNT(*) FROM nav_history;

SELECT COUNT(*) FROM scheme_performance;

SELECT COUNT(*) FROM investor_transactions;
SELECT COUNT(*) AS total_nav_records
FROM nav_history;

SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

SELECT
    AVG(return_1yr_pct) AS avg_return_1yr
FROM scheme_performance;

SELECT
    scheme_name,
    sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM investor_transactions
GROUP BY transaction_type;

SELECT
    AVG(amount_inr) AS avg_transaction_amount
FROM investor_transactions;

SELECT
    risk_grade,
    COUNT(*) AS fund_count
FROM scheme_performance
GROUP BY risk_grade;

SELECT
    fund_house,
    COUNT(*) AS scheme_count
FROM scheme_performance
GROUP BY fund_house
ORDER BY scheme_count DESC;
