
import mysql.connector

def get_connection():
    return mysql.connector.connect(
    host="127.0.0.1",
    user="admin",
    password="Admin@123",
    database="mydb"
    )

if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    print(cursor.fetchall())
    cursor.close()
    conn.close()

