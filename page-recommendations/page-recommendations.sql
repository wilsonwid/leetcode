# Write your MySQL query statement below
SELECT DISTINCT L.page_id AS recommended_page
FROM Likes L, Friendship F
WHERE ((F.user1_id = 1 AND L.user_id = F.user2_id) OR (F.user2_id = 1 AND L.user_id = F.user1_id))   AND L.page_id NOT IN (
    SELECT L1.page_id FROM Likes L1
    WHERE L1.user_id = 1
)
