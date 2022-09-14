# Write your MySQL query statement below
SELECT id ,'Root' AS Type
FROM Tree
WHERE p_id IS NULL
UNION
SELECT id, 'Leaf' as Type
FROM Tree
WHERE
    id NOT IN (
    SELECT DISTINCT p_id 
    FROM Tree
    WHERE p_id IS NOT NULL
    )
    AND p_id IS NOT NULL
UNION
SELECT id,'Inner' as Type
FROM Tree
WHERE
    id IN(
    SELECT DISTINCT p_id
    FROM Tree
    WHERE p_id IS NOT NULL
    )
    AND p_id IS NOT NULL
order by id 


# Write your MySQL query statement below
SELECT id as 'ID',
    CASE
    WHEN id=(SELECT id from tree where p_id is null) THEN 'Root'
    WHEN id in(select p_id from tree) THEN 'Inner'
    ELSE 'Leaf'
    END
    AS Type
FROM Tree

ORDER BY 'ID'