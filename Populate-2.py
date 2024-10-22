import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="adminroot",
    database="alx_book_store"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO customers(customer_id, customer_name, email, address)VALUES(2,'Blessing Malik','bmalik@sandtech.com','124 Happiness  Ave.'),(3,'Obed Ehoneah','eobed@sandtech.com','125 Happiness  Ave.'),(4,'Nehemial Kamolu','nkamolu@sandtech.com','126 Happiness  Ave.')")
mydb.commit()
 
mycursor.close()
mydb.close()
