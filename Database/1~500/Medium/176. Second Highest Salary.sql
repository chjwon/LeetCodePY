# Write your MySQL query statement below
SELECT MAX(Salary) AS SecondHighestSalary FROM Employee
Where Salary < (SELECT Max(Salary) FROM Employee)
