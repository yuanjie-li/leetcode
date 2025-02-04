# Write your MySQL query statement below
SELECT DISTINCT 
    project_id 
    ,ROUND(AVG(experience_years)OVER(PARTITION BY project_id), 2) as average_years 
FROM Project p
JOIN Employee e 
ON 
    p.employee_id = e.employee_id 
