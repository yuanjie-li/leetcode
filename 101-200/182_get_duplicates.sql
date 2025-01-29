SELECT email 
FROM 
(SELECT 
    email
    ,count(id) as cnt 
    FROM Person 
    GROUP BY email 
) g 
WHERE 
cnt > 1 
