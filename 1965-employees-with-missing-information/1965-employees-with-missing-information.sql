# Write your MySQL query statement below
SELECT employee_id FROM     
Employees LEFT JOIN Salaries USING (employee_id)
WHERE salary IS NULL 
UNION
SELECT employee_id FROM     
Salaries LEFT JOIN Employees USING (employee_id)
WHERE name IS NULL 
ORDER BY employee_id;