SELECT c.name, SUM(o.amount) AS total
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.name
HAVING total > 100;
