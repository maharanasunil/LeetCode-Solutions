# Write your MySQL query statement below
/*
MESSED THIS UP WITH BELOW CODE IN 1ST TRY !!!
SELECT o.buyer_id, u.join_date, COUNT(o.item_id) AS orders_in_2019
FROM  Orders o JOIN Items i
USING (item_id)
JOIN Users u
WHERE (u.favorite_brand = i.item_brand AND YEAR(o.order_date) = "2019")
GROUP BY o.buyer_id

Case When Method:(Looks Good)
select  u.user_id as buyer_id,
        u.join_date,
        sum(
            case
                when year(o.order_date)=2019 then 1
                else 0
            end) as orders_in_2019
from users u 
left join orders o on u.user_id = o.buyer_id
group by u.user_id
*/

SELECT 
    u.user_id as buyer_id, 
    u.join_date, 
    IFNULL(COUNT(order_date ),0) AS orders_in_2019 
FROM Users u LEFT JOIN Orders o 
ON (u.user_id = o.buyer_id) AND YEAR(order_date) = "2019"
GROUP BY u.user_id