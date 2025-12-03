# Write your MySQL query statement below
select customer_id, count(Distinct visit_id)as count_no_trans
from Visits where visit_id NOT in (
    select visit_id from Transactions
)
Group by customer_id;
