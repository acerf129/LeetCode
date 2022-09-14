# Write your MySQL query statement below
SELECT actor_id,director_id FROM(
SELECT actor_id,director_id,COUNT(actor_id) counts
FROM ActorDirector
GROUP BY actor_id,director_id
)q
WHERE counts>=3