# Write your MySQL query statement below
SELECT s.name from SalesPerson s
WHERE s.sales_id NOT IN 
(SELECT o.sales_id 
 FROM SalesPerson JOIN Orders o USING (sales_id)
 JOIN Company c USING(com_id)
 WHERE o.com_id = c.com_id AND c.name = 'RED'
)

/*
Explaination:
The first inner join creates a view for just 'RED' orders
The right join ensures all salespersons are included (even those who do not have RED orders)
The WHERE IS NULL gives salespersons who did not have any RED orders due to the right join

select salesperson.name
from orders o join company c on (o.com_id = c.com_id and c.name = 'RED')
right join salesperson on salesperson.sales_id = o.sales_id
where o.sales_id is null
*/