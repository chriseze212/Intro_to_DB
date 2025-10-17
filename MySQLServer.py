#!/usr/bin/python3
"""
This script creates the 'alx_book_store' database in a MySQL server.
If the database already exists, the script will not fail.
"""

import mysql.connector

def create_database():
    connection = None
    try:
        # Connect to MySQL server (update user/password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='nonso'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # Ensure the connection is properly closed
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
