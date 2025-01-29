CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
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
                r = N 
            ) AS SecondHighestSalary
            FROM dual
  );
END
