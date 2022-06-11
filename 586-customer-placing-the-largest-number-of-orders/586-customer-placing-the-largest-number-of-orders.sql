# Write your MySQL query statement below
# The below solution is for the follow up question.

WITH CTE AS
    (
        SELECT customer_number, RANK() OVER(ORDER BY COUNT(1) DESC) AS RANK_val
        FROM Orders 
        GROUP BY customer_number
    )
SELECT customer_number
FROM CTE
WHERE RANK_val = 1;

/*
SELECT 
    customer_number 
FROM 
    Orders 
GROUP BY  customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
*/