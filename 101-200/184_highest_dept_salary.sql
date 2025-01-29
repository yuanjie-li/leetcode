SELECT 
    Department
    ,Employee
    ,Salary
FROM
(
    SELECT 
        Department
        ,Employee
        ,Salary
        ,MAX(Salary)OVER(PARTITION BY Department) AS MaxSalary
    FROM 
    (
        SELECT 
            name AS Employee
            ,Department
            ,Salary
        FROM Employee
        JOIN 
        (
            SELECT 
                id as depID
                ,name as Department
            FROM Department 
        ) dep
        ON 
            depID = DepartmentId
        
    ) depname
) maxsal 
WHERE 
    Salary = MaxSalary
