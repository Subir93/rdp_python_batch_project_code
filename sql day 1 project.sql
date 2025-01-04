show databases;
create database python_project_curd;
use python_project_curd; -- before creating/updating or anything in the databse use this line 
show tables;
create table cust_details (
cust_id int auto_increment primary key,
cust_name varchar(100) not null,
cust_address varchar(255) not null,
cust_phon_no varchar(10) not null,
cust_user_id varchar(50) not null,
cust_password varchar(100) not null
)auto_increment=1;

INSERT INTO cust_details (cust_name, cust_address, cust_phon_no, cust_user_id, cust_password) 
VALUES 
('John Doe', '123 Maple Street, Springfield', '9876543210', 'johndoe', 'password123');

select * from cust_details;
truncate cust_details;

create table audit_table (
sl_no int auto_increment primary key,
cust_name varchar(100) not null,
cust_id varchar(255) not null,
login_time timestamp default current_timestamp,
logout_time timestamp default current_timestamp
)auto_increment=1;
select *from audit_table;
insert into audit_table (cust_id, cust_name,logout_time)
values (101,'John Doe',null);
insert into audit_table (cust_id, cust_name,login_time)
values (101,'John Doe',null);

truncate table audit_table;
drop table audit_table;
