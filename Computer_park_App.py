from flask import Flask, render_template, request
import mysql.connector 

app = Flask(__name__)


def fetch_data(computer_id="", company="", comp_det="", computer_id_del=""):
    
    cnx = mysql.connector.connect(user='root', password='123456789',
                              host='localhost', database='Computer_park')

    # Create a cursor object to execute queries
    cursor = cnx.cursor()

    if len(computer_id) >= 1:
        query = """
        SELECT * 
        FROM rentails     
        JOIN computer_details ON computer_details.model_number = rentails.model_number
        JOIN company_details ON company_details.model_number = rentails.model_number
        WHERE rentails.model_number = %s;
        """
        cursor.execute(query, (computer_id,))

        rows = cursor.fetchall()
        sequence = cursor.column_names
        main_data = [result for result in rows]
        return sequence, tuple(main_data)
        
    if len(company) >= 1:
        query = """
        SELECT * FROM company_details WHERE company_details.company_name = %s;
        """
        cursor.execute(query, (company,))

        rows = cursor.fetchall()
        sequence = cursor.column_names
        main_data = [result for result in rows]
        return sequence, tuple(main_data)
    
    if len(comp_det) > 1:
        model, ram, storage, processor = comp_det.split(",")
        query = """
        INSERT INTO Computer_Park.computer_details (model_number, ram, Storage, processor)
        VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (model, ram, storage, processor))
        cnx.commit()

        query = """
        SELECT * FROM computer_details;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        sequence = cursor.column_names
        main_data = [result for result in rows]
        return sequence, tuple(main_data)
    
    if len(computer_id_del) >= 1:
        query = """
            DELETE FROM computer_details 
            WHERE computer_details.model_number = %s;
            """
        cursor.execute(query, (computer_id_del,))
        cnx.commit()

        query = """
        SELECT * FROM computer_details;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        sequence = cursor.column_names
        main_data = [result for result in rows]
        return sequence, tuple(main_data)

    
@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "POST":
        computer_id = request.form['computer_id']
        company = request.form['company']
        comp_det = request.form['comp_det']
        computer_id_del = request.form['computer_id_del']
        print(computer_id, company, comp_det, computer_id_del)
        headings, data = fetch_data(computer_id, company, comp_det, computer_id_del)
        return render_template("Main_page.html", headings=headings, data=data)
    return render_template("Main_page.html")


if __name__=="__main__":
    app.run(debug=True)
