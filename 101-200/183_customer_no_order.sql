SELECT name as Customers 
FROM Customers 
WHERE 
id not in (select distinct customerId from orders)
