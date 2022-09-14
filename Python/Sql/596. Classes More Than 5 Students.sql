# Write your MySQL query statement below
SELECT class FROM(
SELECT class ,COUNT(student)counts
FROM  Courses
GROUP BY class
)q
WHERE counts >=5