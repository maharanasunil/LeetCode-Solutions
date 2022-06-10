# Write your MySQL query statement below
SELECT w1.id AS id 
FROM Weather w1, Weather w2
WHERE w1.temperature > w2.temperature 
AND
DATEDIFF(w1.recordDate, w2.recordDate) = 1

/*
USING LAG:

SELECT id FROM(
    SELECT *,
    LAG(temperature) OVER(ORDER BY recordDate) AS prevT,
    DATEDIFF(recordDate, LAG(recordDate) OVER(ORDER BY recordDate)) AS Delta
    FROM Weather) t
WHERE Delta = 1 AND temperature>prevT
*/