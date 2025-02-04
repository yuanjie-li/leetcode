# Write your MySQL query statement below
SELECT 
    contest_id
    ,ROUND(100. * COUNT(user_id) / all_users, 2) AS percentage 
FROM Register r 
CROSS JOIN 
(
    SELECT 
        COUNT(*) AS all_users 
    FROM Users  
) u 

GROUP BY contest_id
ORDER BY percentage DESC, contest_id 
