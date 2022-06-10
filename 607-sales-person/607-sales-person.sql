# Write your MySQL query statement below
SELECT s.name from SalesPerson s
WHERE s.sales_id NOT IN 
(SELECT o.sales_id 
 FROM SalesPerson JOIN Orders o USING (sales_id)
 JOIN Company c USING(com_id)
 WHERE o.com_id = c.com_id AND c.name = 'RED'
)