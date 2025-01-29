SELECT Id
FROM 
(
    SELECT 
        id
        ,LAG(temperature, 1, NULL) OVER(ORDER BY recordDate) - temperature AS TempDiff
        ,LAG(recordDate, 1, NULL) OVER(ORDER BY recordDate) prevDate
        ,recordDate
    FROM 
        Weather 
) w
WHERE 
    TempDiff < 0
    AND
    DATEDIFF(recordDate, prevDate) = 1
