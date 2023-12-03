CREATE TABLE Computer_park.computer_details(
    model_number varchar(50) primary key,
    ram int,
    Storage varchar(50),
    processor varchar(50)
);



CREATE TABLE Computer_park.company_details(
    model_number varchar(50),
    company_name varchar(50),
    MRP DOUBLE,
    discount_price DOUBLE,
);


CREATE TABLE Computer_park.customer_details(
    customer_name varchar(50),
    model_number varchar(50),
    customer_address varchar(100),
    customer_number BIGINT
);



CREATE TABLE Computer_park.rentails(
model_number varchar(50),
price float,
details varchar(50),
duration int
);
