# Write your MySQL query statement below
select customer_id, Count(Visits.visit_id) as count_no_trans
from Visits LEFT JOIN  Transactions Using(visit_id)
where Transactions.visit_id is NULL group by customer_id;