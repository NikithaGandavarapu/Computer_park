INSERT INTO Computer_Park.computer_details (model_number, ram, Storage , processor)
VALUES ('MARK15', '16', 'SSD 1TB', 'M1 Chip');

INSERT INTO Computer_Park.computer_details (model_number, ram, Storage , processor)
VALUES ('MARK20', '16', 'SSD 2TB', 'M2 Chip');

INSERT INTO Computer_Park.computer_details (model_number, ram, Storage , processor)
VALUES ('Ionic156', '8', 'SSD 512GB', 'Intel 8 Core');

INSERT INTO Computer_Park.computer_details (model_number, ram, Storage , processor)
VALUES ('M124567', '8', 'SSD 512GB', 'Intel QuadCore');

INSERT INTO Computer_Park.computer_details (model_number, ram, Storage , processor)
VALUES ('M12345', '16', 'SSD 1TB', 'AMD Ryzen');



ALTER TABLE Computer_Park.rentails CHANGE price price DOUBLE;

INSERT INTO Computer_Park.company_details (model_number, company_name, MRP , discount_price)
VALUES ('MARK15', 'Apple', 100000.00, 80000.0);

INSERT INTO Computer_Park.company_details (model_number, company_name, MRP , discount_price)
VALUES ('MARK20', 'Apple', 140000.00, 110000.00);

INSERT INTO Computer_Park.company_details (model_number, company_name, MRP , discount_price)
VALUES ('Ionic156', 'Intel', 65000.00, 60000.00);

INSERT INTO Computer_Park.company_details (model_number, company_name, MRP , discount_price)
VALUES ('M124567', 'MSI', 80000.00, 70000.00);

INSERT INTO Computer_Park.company_details (model_number, company_name, MRP , discount_price)
VALUES ('M12345', 'MSI', 95000.00, 85000.00);




INSERT INTO Computer_Park.rentails (model_number, price, details , duration)
VALUES ('MARK15', 5000.00, 'RENT', 30);

INSERT INTO Computer_Park.rentails (model_number, price, details , duration)
VALUES ('MARK20', 0, 'BUY', 0);

INSERT INTO Computer_Park.rentails (model_number, price, details , duration)
VALUES ('Ionic156', 3500.00, 'RENT', 30);

INSERT INTO Computer_Park.rentails (model_number, price, details , duration)
VALUES ('M124567', 10000, 'RENT', 60);

INSERT INTO Computer_Park.rentails (model_number, price, details , duration)
VALUES ('M12345', 0, 'BUY', 0);


INSERT INTO Computer_Park.customer_details(customer_name, model_number, customer_address, customer_number) 
VALUES ('Chakrapani', 'MARK15', '123 Sunshine Avenue, Mumbai, Maharashtra, India', 7845961205);

INSERT INTO Computer_Park.customer_details(customer_name, model_number, customer_address, customer_number) 
VALUES ('Nikitha', 'MARK20', '567 Serenity Street, Chennai, Tamil Nadu, India', 7856461105);

INSERT INTO Computer_Park.customer_details(customer_name, model_number, customer_address, customer_number) 
VALUES ('Hema', 'Ionic156', '789 Harmony Road, Delhi, Delhi, India', 9396405586);

INSERT INTO Computer_Park.customer_details(customer_name, model_number, customer_address, customer_number) 
VALUES ('Indranath', 'M124567', '56 Tranquil Lane, Bangalore, Karnataka, India', 9963963025);

INSERT INTO Computer_Park.customer_details(customer_name, model_number, customer_address, customer_number) 
VALUES ('Manoj', 'M12345', '321 Peaceful Circle, Kolkata, West Bengal, India', 7670954218);
