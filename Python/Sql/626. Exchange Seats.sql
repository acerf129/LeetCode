# Write your MySQL query statement below
SELECT 
    CASE
    WHEN id%2=1 and counts!=id  THEN id+1
    WHEN id %2=1 and counts=id  THEN id 
    ELSE id-1
    END
    AS id,
    student
FROM SEAT,
(SELECT COUNT(*) as counts
FROM SEAT)seatCount
order by id ;