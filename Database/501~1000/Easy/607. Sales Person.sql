# Write your MySQL query statement below
SELECT S.name
FROM SalesPerson S
WHERE S.sales_id not in (
    SELECT O.sales_id
    FROM Orders O
    LEFT JOIN Company C
        ON O.com_id = C.com_id
        WHERE C.name = 'RED'
)