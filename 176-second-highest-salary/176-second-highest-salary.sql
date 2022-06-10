# Write your MySQL query statement below
WITH CTE AS
(SELECT salary, dense_rank() over(ORDER BY salary DESC) AS RANK_desc
 FROM Employee)
 
 SELECT MAX(salary) AS SecondHighestSalary  FROM CTE
 WHERE RANK_desc = 2;