# Write your MySQL query statement below
 SELECT u.user_id as buyer_id,join_date, 
 COUNT(CASE WHEN o.order_date BETWEEN '2019-01-01' and '2019-12-31' THEN 1 ELSE NULL END)as orders_in_2019
 FROM Users u
 LEFT JOIN Orders o  ON u.user_id =o.buyer_id
 LEFT JOIN Items i  ON o.item_id=i.item_id
 GROUP BY u.user_id