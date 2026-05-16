SELECT COUNT(*) AS completed_orders_count
FROM orders
WHERE status = 'completed';
