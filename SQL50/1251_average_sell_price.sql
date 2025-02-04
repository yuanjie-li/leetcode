# Write your MySQL query statement below
SELECT 
    p.product_id
    ,ROUND(SUM(price * IFNULL(units, 0)) / IFNULL(SUM(units), 1), 2) AS average_price
FROM Prices p
LEFT JOIN UnitsSold s 
ON 
    s.product_id = p.product_id 
    AND 
    s.purchase_date between p.start_date and p.end_date

GROUP BY p.product_id
ORDER BY p.product_id
