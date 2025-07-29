show databases;


use sql12792572;

create table signup(
username varchar(120)unique, 
fullname  varchar(255),
phone_number varchar(12),
email varchar(255),
passwordd varchar (255)
);

-- insert into signup(username, fullname, phone_number, email, passwordd) values

select * from signup;


create table mytodosonline(
todo_id int auto_increment unique,
todo_added varchar(255),
todo_title varchar(255),
todo_desc text);



select * from mytodosonline;




