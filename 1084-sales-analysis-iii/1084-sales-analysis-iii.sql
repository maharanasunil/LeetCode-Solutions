# Write your MySQL query statement below
/*
SELECT
    product_id,
    product_name 
FROM Product
WHERE 
product_id IN (
    SELECT product_id FROM Sales
    GROUP BY product_id
    HAVING (MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31')
)
*/

SELECT
    p.product_id,
    product_name 
FROM Product p JOIN Sales s
USING(product_id)
GROUP BY p.product_id
HAVING (MIN(s.sale_date) >= '2019-01-01' 
        AND MAX(s.sale_date) <= '2019-03-31')