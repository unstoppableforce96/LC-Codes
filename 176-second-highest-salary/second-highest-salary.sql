/* Write your PL/SQL query statement below */
SELECT MAX(salary) AS SecondHighestSalary FROM employee
WHERE salary < (SELECT MAX(salary) FROM employee);