SELECT
    customer_id,
    total_revenue
FROM sales_mart
ORDER BY total_revenue DESC
LIMIT 10;

SELECT
    order_date,
    SUM(total_amount) AS daily_revenue
FROM sales
GROUP BY order_date
ORDER BY order_date;
