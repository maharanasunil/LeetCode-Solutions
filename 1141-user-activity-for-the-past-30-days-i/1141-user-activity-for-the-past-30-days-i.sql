# Write your MySQL query statement below
SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity 
WHERE 
    DATEDIFF('2019-07-27', activity_date) < 30
    AND activity_date <= '2019-07-27'
GROUP BY
    activity_date

/*
GROUP BY activity_date 
HAVING activity_date BETWEEN '2019-06-28' and '2019-07-27'
*/
#  Datediff(date1, date2) = date1 - date2