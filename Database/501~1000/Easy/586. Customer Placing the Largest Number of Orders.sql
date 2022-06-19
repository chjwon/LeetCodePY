# Write your MySQL query statement below
SELECT customer_number
FROM Orders O
GROUP BY customer_number
ORDER BY Count(*) DESC
LIMIT 1;