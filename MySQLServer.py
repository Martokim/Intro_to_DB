#!/usr/bin/python3
import mysql.connector #comment: Ensure you have mysql-connector-python installed

def create_database():
    connection = None
    try:
        # Connect to MySQL server (no DB specified yet)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_mysql_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
