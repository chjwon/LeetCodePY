# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person P
LEFT JOIN Address A
    On P.personId = A.personId;