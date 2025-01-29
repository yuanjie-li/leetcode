SELECT 
    name AS Employee 
FROM Employee 
JOIN
(
    SELECT 
        id as manId
        ,salary as manSalary
    FROM Employee 
) man 

ON 
    managerId = manId 

WHERE 
    salary > manSalary
