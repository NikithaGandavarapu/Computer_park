The provided SQL queries and data describe a database named "Computer_Park" that manages information about computer rentals, computer details, company details, and customer details. Let's break down the components:

### Tables:

1. **computer_details:**
   - Fields: `model_number` (primary key), `ram`, `Storage`, `processor`.
   - Example records for different computer models like 'MARK15', 'MARK20', 'Ionic156', 'M124567', 'M12345'.

2. **company_details:**
   - Fields: `model_number`, `company_name`, `MRP`, `discount_price`.
   - Example records containing information about companies like Apple, Intel, and MSI.

3. **rentails:**
   - Fields: `model_number`, `price`, `details`, `duration`.
   - Example records indicating rental information for different computer models.

4. **customer_details:**
   - Fields: `customer_name`, `model_number`, `customer_address`, `customer_number`.
   - Example records associating customers with specific computer models they are interested in.

### Queries:

- A SELECT query is used to retrieve information about a specific computer model ('M12345') from the rental database, including details from both the `rentails` and related tables (`computer_details` and `company_details`).

### Descriptions:

1. **Computer Details:**
   - Information about various computer models, including details like RAM, storage, and processor.

2. **Company Details:**
   - Details about different companies, including the model numbers of the computers they manufacture, the Manufacturer's Retail Price (MRP), and discounted prices.

3. **Rental Information:**
   - Records of computer rentals, specifying the model, price, rental details, and duration. Some computers are also available for purchase ('BUY' with a price of 0).

4. **Customer Details:**
   - Information about customers, including their names, the model of the computer they are interested in, addresses, and contact numbers.

### Sample Scenarios:

- The 'MARK15' model from Apple (MRP: $100,000, Discount Price: $80,000) is available for rent at $5,000 for 30 days and has been rented by a customer named Chakrapani.

- The 'M12345' model from MSI (MRP: $95,000, Discount Price: $85,000) is available for both rent (priced at $0 for 0 days) and purchase (priced at $0), and it has been purchased by a customer named Manoj.

This database appears to facilitate the management of computer rentals, purchases, and customer interactions, providing a comprehensive view of computer-related transactions and customer relationships within the "Computer_Park" system.
