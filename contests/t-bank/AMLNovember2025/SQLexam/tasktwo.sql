SELECT city
FROM (
  SELECT c.city,
         SUM(o.total) AS revenue
  FROM customers AS c
  JOIN orders AS o ON o.cust_id = c.cust_id
  WHERE o.status = 'completed'
  GROUP BY c.city
) AS by_city
ORDER BY revenue DESC, city ASC
LIMIT 1;