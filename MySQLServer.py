import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="adminroot",
    )
    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("'alx_book_store' created successfully!")

    except Error ase:

        print("Error: failed to cennect to data base")

    finally:
        if connection.is_connected():
            cursor.close()
            mydb.close()
            print("connection closed")

