CREATE TABLE IF NOT EXISTS sales_mart AS
SELECT
    customer_id,
    COUNT(order_id) AS orders_count,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_order_value
FROM sales
GROUP BY customer_id;
