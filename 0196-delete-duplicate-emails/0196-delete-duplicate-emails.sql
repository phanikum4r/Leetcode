# Write your MySQL query statement below
Delete p from person p
left join 
(select min(id) as id from person 
group by email) q
on p.id = q.id
where q.id is null;