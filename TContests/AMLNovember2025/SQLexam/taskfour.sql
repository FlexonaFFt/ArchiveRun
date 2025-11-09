WITH completed_orders AS (
  SELECT restaurant, cust_id
  FROM orders
  WHERE status = 'completed'
),
repeat_clients_per_restaurant AS (
  SELECT restaurant,
         COUNT(*) AS repeat_clients
  FROM (
    SELECT restaurant, cust_id
    FROM completed_orders
    GROUP BY restaurant, cust_id
    HAVING COUNT(*) >= 2
  ) rc
  GROUP BY restaurant
),
completed_counts AS (
  SELECT restaurant,
         COUNT(*) AS completed_orders_total
  FROM completed_orders
  GROUP BY restaurant
)
SELECT r.restaurant
FROM repeat_clients_per_restaurant r
JOIN completed_counts c USING (restaurant)
ORDER BY r.repeat_clients DESC,
         c.completed_orders_total DESC,
         r.restaurant ASC
LIMIT 1;