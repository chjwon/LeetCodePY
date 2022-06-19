# Write your MySQL query statement below
SELECT name
FROM Customer C
WHERE C.referee_id != 2 or C.referee_id is null;