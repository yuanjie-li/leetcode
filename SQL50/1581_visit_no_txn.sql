SELECT 
    customer_id
    ,COUNT(customer_id) as count_no_trans
FROM 
    Visits v
WHERE 
    visit_id not in (SELECT DISTINCT visit_id FROM Transactions)

GROUP BY customer_id 
