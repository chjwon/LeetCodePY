# Write your MySQL query statement below
SELECT name, population, area FROM World AS W
WHERE W.population >= 25000000 or W.area >= 3000000;