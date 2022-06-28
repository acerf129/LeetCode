# Write your MySQL query statement below

Select D.Name as Department,E1.Name as Employee,E1.Salary as Salary

From Employee as E1,Department as D
Where (
    Select Count(Distinct E2.Salary)
    From Employee as E2
    Where E1.DepartmentId=E2.DepartmentId and E2.Salary>E1.Salary
)<3
and E1.DepartmentId=D.Id