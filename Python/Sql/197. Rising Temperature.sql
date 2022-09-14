SELECT w1.id as 'Id'
FROM Weather w1,Weather w2
WHERE w1.temperature>w2.temperature and TO_DAYS(w1.recordDate)-TO_DAYS(w2.recordDate)=1