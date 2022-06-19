# Write your MySQL query statement below
SELECT product_id, product_name
FROM Product
WHERE product_id not in
(SELECT product_id FROM Sales
 WHERE sale_date > '2019-03-31' OR sale_date < '2019-01-01' )
 
 
