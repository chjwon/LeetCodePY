# Write your MySQL query statement below
SELECT class FROM Courses AS C
GROUP BY class
HAVING Count(*) > 4;