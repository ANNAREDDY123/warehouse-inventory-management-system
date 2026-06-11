
-- 1. Total Products


SELECT COUNT(*) AS total_products
FROM products;



-- 2. Low Stock Products


SELECT *
FROM products
WHERE stock_quantity < 10;



-- 3. Total Stock Available

SELECT
    SUM(stock_quantity) AS total_stock
FROM products;



-- 4. Products By Category


SELECT
    category,
    COUNT(*) AS total_products
FROM products
GROUP BY category;



-- 5. Stock Added (INWARD)


SELECT
    product_id,
    SUM(quantity) AS total_added
FROM stock_history
WHERE movement_type = 'INWARD'
GROUP BY product_id;



-- 6. Stock Removed (OUTWARD)


SELECT
    product_id,
    SUM(quantity) AS total_removed
FROM stock_history
WHERE movement_type = 'OUTWARD'
GROUP BY product_id;



-- 7. Product Stock Movement History


SELECT
    p.product_name,
    s.movement_type,
    s.quantity,
    s.created_at
FROM stock_history s
JOIN products p
ON p.id = s.product_id
ORDER BY s.created_at DESC;



-- 8. Supplier Count


SELECT COUNT(*) AS total_suppliers
FROM suppliers;



-- 9. Most Active Product


SELECT
    product_id,
    COUNT(*) AS movements
FROM stock_history
GROUP BY product_id
ORDER BY movements DESC;



-- 10. Rank Products By Stock


SELECT
    product_name,
    stock_quantity,
    RANK() OVER(
        ORDER BY stock_quantity DESC
    ) AS stock_rank
FROM products;
