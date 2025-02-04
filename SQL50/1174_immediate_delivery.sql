# Write your MySQL query statement below
SELECT 
ROUND(100. * SUM(IF(order_date = customer_pref_delivery_date, 1., 0.)) / COUNT(*) ,2) as immediate_percentage 
FROM 
(
    SELECT * 
    ,rank()OVER(PARTITION BY customer_id ORDER BY order_date) AS r
    FROM 
    Delivery  
) d
WHERE r = 1 
