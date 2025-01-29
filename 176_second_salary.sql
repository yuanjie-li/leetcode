SELECT 
(SELECT 
    salary 
    FROM 
    (
    SELECT DISTINCT  
        salary 
        ,
        DENSE_RANK() OVER( ORDER BY salary DESC ) r
    FROM 
        Employee 
    ) s 
    WHERE 
    r = 2 
) AS SecondHighestSalary
FROM dual
