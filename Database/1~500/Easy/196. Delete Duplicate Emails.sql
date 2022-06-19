# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE n1
FROM Person n1, Person n2
WHERE n1.id > n2.id AND n1.email = n2.email;