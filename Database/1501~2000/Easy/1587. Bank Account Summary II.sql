# Write your MySQL query statement below
SELECT U.name, SUM(t.amount) AS balance
FROM Transactions T
LEFT JOIN Users U
    ON U.account = T.account
GROUP BY U.account
HAVING SUM(t.amount) > 10000
