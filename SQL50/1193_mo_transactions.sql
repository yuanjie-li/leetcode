SELECT 
    SUBSTRING(trans_date, 1, 7) AS month
    ,country
    ,COUNT(id) as trans_count
    ,SUM(IF(state = 'approved', 1, 0)) AS approved_count 
    ,SUM(amount) as trans_total_amount
    ,SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount 
FROM Transactions 
GROUP BY country, SUBSTRING(trans_date, 1, 7) 
