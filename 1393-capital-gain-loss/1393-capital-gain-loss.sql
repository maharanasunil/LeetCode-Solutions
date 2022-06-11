# Write your MySQL query statement below
SELECT
    stock_name,
    SUM(
        CASE WHEN operation = 'Buy' THEN -price
        ELSE price
        END
    ) AS capital_gain_loss 
FROM Stocks
GROUP BY stock_name

/*
Do sum of(Sell) - sum of(Buy) to get proper answer.
SUM(IF(operation = 'Sell', price, 0)) - SUM(IF(operation = 'Buy', price, 0))
*/