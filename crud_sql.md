SELECT * 
        FROM rentails     
        JOIN computer_details ON computer_details.model_number = rentails.model_number
        JOIN company_details ON company_details.model_number = rentails.model_number
        WHERE rentails.model_number = %s;


SELECT * FROM company_details WHERE company_details.company_name = %s;


 INSERT INTO Computer_Park.computer_details (model_number, ram, Storage, processor)
        VALUES (%s, %s, %s, %s);


DELETE FROM computer_details 
            WHERE computer_details.model_number = %s;
