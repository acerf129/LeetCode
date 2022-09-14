# Write your MySQL query statement below
SELECT player_id,event_date as first_login
FROM (
    SELECT player_id,event_date,rank() over(partition by player_id order by event_date) as rankNo
    FROM Activity
)q
WHERE rankNo=1

SELECT player_id,min(event_date) as first_login
FROM Activity
GROUP BY player_id