# Write your MySQL query statement below
SELECT stock_name, SUM(if (operation='BUY',-price,price)) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name