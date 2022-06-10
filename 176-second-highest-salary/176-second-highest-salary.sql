# Write your MySQL query statement below

WITH CTE AS
			(SELECT Salary, DENSE_RANK () OVER (ORDER BY Salary desc) AS RANK_desc
			   FROM Employee)
SELECT MAX(salary) AS SecondHighestSalary
  FROM CTE
 WHERE RANK_desc = 2
 /*
WITH cte AS 
    (
        SELECT salary, RANK() OVER (ORDER BY salary DESC) as rank
    FROM Employee
    )

SELECT MAX(salary) AS SecondHighestSalary 
FROM cte
WHERE rank=2;
*/
