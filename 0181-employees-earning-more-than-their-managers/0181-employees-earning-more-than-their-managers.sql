# Write your MySQL query statement below
-- select name as Employee from employee a
-- where (select salary from employee b where a.managerid = b.id) < a.salary;
select a.name as Employee
from employee a join employee b
on a.managerid = b.id
where a.salary > b.salary;