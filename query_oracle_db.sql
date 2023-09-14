SELECT
    TO_CHAR(o.order_date, 'YYYY-MM') AS month,
    c.customer_id,
    COUNT(o.order_id) AS orders_quantity,
    SUM(o.quantity) AS total_quantity,
    ROUND(SUM(o.sales) / SUM(o.QUANTITY),2) AS price,
    SUM(o.sales) AS total_sales,
    SUM(o.profit) AS total_profit,
    SUM(o.sales) - SUM(O.PROFIT) as total_cost,
    ROUND((SUM(o.sales) - SUM(O.PROFIT)) / SUM(o.QUANTITY),2) as unit_cost,
    ROUND(SUM(o.PROFIT) / sum(o.SALES), 2)*100 || '%' as margin,
    SUM(o.discount) AS total_discount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
GROUP BY TO_CHAR(o.order_date, 'YYYY-MM'), c.CUSTOMER_ID

ORDER BY month ASC;


SELECT
    c.customer_id,
    COUNT(o.order_id) AS orders_quantity,
    SUM(o.quantity) AS total_quantity,
    ROUND(SUM(o.sales) / SUM(o.QUANTITY),2) AS price,
    SUM(o.sales) AS total_sales,
    SUM(o.profit) AS total_profit,
    SUM(o.sales) - SUM(O.PROFIT) as total_cost,
    ROUND((SUM(o.sales) - SUM(O.PROFIT)) / SUM(o.QUANTITY),2) as unit_cost,
    ROUND(SUM(o.PROFIT) / sum(o.SALES), 4)*100 || '%' as margin
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
HAVING c.CUSTOMER_ID LIKE 'SC_%'
GROUP BY c.CUSTOMER_ID