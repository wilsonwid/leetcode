SELECT u.product_id, ROUND(SUM(u.units * p.price)/SUM(u.units), 2) AS average_price
FROM UnitsSold u
LEFT JOIN Prices p ON u.product_id = p.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY u.product_id
