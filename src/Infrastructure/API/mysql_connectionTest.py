import mysql.connector

#This class work for testing you Connection between your local db
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hy1aj16",
        database="localmysqldb"
    )
    if conn.is_connected():
        print("✅ `mysql-connector` Connected!")
except mysql.connector.Error as err:
    print(f"❌ `mysql-connector`  Error: {err}")
finally:
    if conn.is_connected():
        conn.close()