# Write your MySQL query statement below
SELECT
    name,
    COALESCE(SUM(amount),0) AS balance
FROM Users JOIN Transactions
USING (account)
GROUP BY account
HAVING (balance > 10000)