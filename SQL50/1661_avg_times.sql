SELECT 
    machine_id
    ,ROUND(AVG(processing_time), 3) AS processing_time
FROM 
(
    SELECT 
        a_init.machine_id 
        ,a_init.process_id
        ,a_stop.timestamp - a_init.timestamp AS processing_time
    FROM Activity a_stop  
    JOIN Activity a_init
    ON 
        a_init.machine_id = a_stop.machine_id
        AND
        a_init.process_id = a_stop.process_id
        AND 
        a_init.activity_type = 'start'
        
    WHERE 
        a_stop.activity_type = 'end'
) times 

GROUP BY machine_id 
