# Write your MySQL query statement below
SELECT
    name AS Customers
FROM Customers C
where C.Id not in (
    SELECT customerId from Orders
);