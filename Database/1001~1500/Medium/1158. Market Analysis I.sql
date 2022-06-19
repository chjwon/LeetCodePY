# Write your MySQL query statement below
SELECT 
    Users.user_id AS buyer_id, 
    Users.join_date, 
    IFNULL(COUNT(order_date),0) AS orders_in_2019
FROM USERS
LEFT JOIN Orders
    ON Orders.buyer_id = Users.user_id AND year(Orders.order_date) = 2019
GROUP BY user_id
ORDER BY user_id