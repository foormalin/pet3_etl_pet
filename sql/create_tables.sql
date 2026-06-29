CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER,
    customer_id INTEGER,
    product_id INTEGER,
    order_date DATE,
    quantity INTEGER,
    price NUMERIC(10, 2),
    total_amount NUMERIC(10, 2)
);
