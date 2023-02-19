SELECT S.seller_name AS SELLER_NAME
FROM Seller S
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders O, Customer C
    WHERE S.seller_id = O.seller_id AND O.customer_id = C.customer_id
    AND YEAR(O.sale_date) = 2020
)
ORDER BY S.seller_name ASC
