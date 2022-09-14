# Write your MySQL query statement below
SELECT name 
FROM SalesPerson
WHERE name not in(
SELECT s.name as name
FROM SalesPerson s
LEFT JOIN Orders o on s.sales_id=o.sales_id
LEFT JOIN Company c on c.com_id=o.com_id
WHERE c.name="RED"
)