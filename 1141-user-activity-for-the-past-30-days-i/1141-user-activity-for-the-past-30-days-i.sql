# Write your MySQL query statement below
SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity 
group by activity_date having activity_date between '2019-06-28' and '2019-07-27'

/*
WHERE 
    DATEDIFF('2019-07-27',activity_date) < 30
GROUP BY
    activity_date
*/
#  Datediff(date1, date2) = date1 - date2