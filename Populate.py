import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="adminroot",
    database="alx_book_store"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO customers(customer_id, customer_name, email, address)VALUES (1,'Cole Baidoo','cbaidoo@sandtech.com','123 Happiness Ave.')")
mydb.commit()
 
mycursor.close()
mydb.close()
