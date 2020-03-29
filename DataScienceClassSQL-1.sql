use classicmodels;
-- exercise 1 for sql basics
select * from customers where city = 'Berlin';
-- exercise 2 for sql basics
select count(*) from customers where country = 'germany';
-- exercise 3
select count(*) from customers where country = 'australia';
-- exercise 4
select customerNumber, customerName from customers where city = 'madrid';
select * from customers where state = 'ca' or country = 'usa';
select * from customers where city = 'berlin'  and country = 'germany';
select * from customers where country != 'usa' and country != 'germany';
select * from customers where country not in ('usa','germany');
select * from customers where country = 'germany' and ( city = 'berlin' or city like 'm%');
select distinct country from customers order by country asc;
insert into customers(customerNumber, City, Country) values(497, 'Stavanger', 'Norway');
select max(customerNumber) from customers;
select distinct city from customers order by customerNumber asc;

