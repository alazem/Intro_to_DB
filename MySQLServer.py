import mysql.connector
from mysql.connector import Error

def create_connection():
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd="Y7$kq9Lp@2mXz")
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database created successfully") 
    except mysql.connector.Error as e:
        print(f"The MySQLServer error '{e}' occurred")
    except Error as e:
        print(f"The error '{e}' occurred")
    finally:
        # Close connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")

# Run the function
if __name__ == "__main__":
    create_connection()