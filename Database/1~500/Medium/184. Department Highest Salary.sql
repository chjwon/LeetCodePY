# Write your MySQL query statement below
SELECT 
    Department.name AS Department,
    E1.name AS Employee,
    E1.salary AS Salary

FROM Department
JOIN Employee E1
    ON E1.departmentId = Department.id
WHERE E1.salary = (SELECT MAX(Salary) FROM Employee E2 
            WHERE E2.departmentId = E1.departmentId)