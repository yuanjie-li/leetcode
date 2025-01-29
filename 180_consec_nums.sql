SELECT DISTINCT 
    num as ConsecutiveNums
FROM 
(
  SELECT 
    num
    ,num - lead(num, 1, NULL) OVER(ORDER BY id) lead1
    ,num - lead(num, 2, NULL) OVER(ORDER BY id) lead2
  
    FROM Logs
) l
WHERE 
  lead1 = 0 
  and 
  lead2 = 0 
