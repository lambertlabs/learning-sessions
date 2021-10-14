\timing
select id from users where id=1000;
select name from users where name='Mary 1000';
create index name_index on users (name);
select name from users where name='Roy 5000';
select name from users where name like '%Linda 300%';
