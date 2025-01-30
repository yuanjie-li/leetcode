# Write your MySQL query statement below
SELECT 
    user_id 
    ,IFNULL(ROUND(AVG(conf_int), 2), 0) AS confirmation_rate 
FROM Signups 
LEFT JOIN 
(
    SELECT 
        user_id as conf_id 
        ,CASE WHEN action = 'confirmed'
        THEN 1
        ELSE 0 END AS conf_int
    FROM Confirmations 
) confs
ON
user_id = conf_id 

GROUP BY user_id

ORDER BY user_id
