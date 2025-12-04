# Write your MySQL query statement below
select name, bonus from Employee LEFT JOIN Bonus using(empId)
where COALESCE(bonus, 0) < 1000;