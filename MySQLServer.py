"""
Write a simple python script that creates the database alx_book_store in your MySQL server.

Name of python script should be MySQLServer.py
If the database alx_book_store already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements
NOTE :

Required to print message such as Database 'alx_book_store' created successfully! when database is successfully created.

Print error message to handle errors when failing to connect to the DB.

handle open and close of the DB in your script.
"""
#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (no DB specified yet)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Mysql_101'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        
    finally:
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
