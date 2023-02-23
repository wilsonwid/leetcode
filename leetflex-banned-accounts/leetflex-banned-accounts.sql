# Write your MySQL query statement below
SELECT DISTINCT l.account_id
FROM LogInfo l
LEFT JOIN LogInfo l1 ON l.account_id = l1.account_id
WHERE l.ip_address <> l1.ip_address AND l1.login <= l.logout AND l.login <= l1.login
