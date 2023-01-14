SELECT u.name, SUM(amount) AS balance
FROM Users u
LEFT JOIN Transactions t ON u.account = t.account
GROUP BY u.account
HAVING SUM(amount) > 10000
