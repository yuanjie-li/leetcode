SELECT 
    unique_id 
    ,name 
FROM Employees e
LEFT JOIN EmployeeUNI u
on
e.id = u.id
