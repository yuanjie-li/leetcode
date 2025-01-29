SELECT 
    Department
    ,Employee
    ,Salary 
FROM 
(
    SELECT 
        Department
        ,Name As Employee
        ,Salary
        ,DENSE_RANK() OVER(PARTITION BY DepartmentID ORDER BY Salary DESC) r
    FROM 
        Employee 
    JOIN 
        (SELECT 
            id AS DepID
            ,name as Department 
        FROM Department
        ) d
    ON 
        DepID = DepartmentID 
) e

WHERE 
r <= 3
