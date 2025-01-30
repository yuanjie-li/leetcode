# Write your MySQL query statement below
SELECT 
    name 
FROM Employee
WHERE 
id in (
    SELECT 
        managerId 
    FROM 
    (
        SELECT 
            managerId
            ,COUNT(managerId) AS count
        FROM Employee 
        GROUP BY managerId 
    ) cnt 
    WHERE 
        count >= 5
)
