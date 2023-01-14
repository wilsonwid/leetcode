SELECT p.product_id, p.product_name
FROM Product p
LEFT JOIN Sales s ON p.product_id = s.product_id
GROUP BY p.product_id
HAVING SUM(s.sale_date NOT BETWEEN "2019-01-01" AND "2019-03-31") = 0
