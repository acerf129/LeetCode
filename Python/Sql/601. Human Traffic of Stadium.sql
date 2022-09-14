# Write your MySQL query statement below
SELECT distinct s1.*
FROM Stadium s1, Stadium s2,Stadium s3
WHERE s1.people>=100 and s2.people>=100 and s3.people>=100
and (
    ((s1.id-s2.id)=1 and (s2.id-s3.id)=1 and (s1.id-s3.id)=2) OR
    ((s1.id-s3.id)=1 and (s2.id-s3.id)=2 and (s2.id-s1.id)=1) OR
    ((s3.id-s2.id)=1 and (s2.id-s1.id)=1 and (s3.id-s1.id)=2) 
)
order by s1.id