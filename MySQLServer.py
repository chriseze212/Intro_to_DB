#!/usr/bin/python3
"""
This script creates the 'alx_book_store' database in a MySQL server.
If the database already exists, the script will not fail.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust host, user, and password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password_here'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close connection properly
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Uncomment next line if you want confirmation message
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
