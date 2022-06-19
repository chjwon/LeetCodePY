# Write your MySQL query statement below
SELECT table1.name AS Employee
FROM Employee as table1
LEFT JOIN Employee as table2
ON table1.managerId = table2.id
WHERE table1.salary > table2.salary;