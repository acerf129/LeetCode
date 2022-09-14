# Write your MySQL query statement below
SELECT c.name as 'Customers'

FROM Customers as c
WHERE c.id not in (
    Select DISTINCT customerId from Orders
)