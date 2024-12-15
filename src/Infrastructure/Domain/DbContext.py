import pyodbc

from API.DbConfig import DbConfig

class DbContext:
    def __init__(self, config: DbConfig):
        self.config = config
        self.conn = None

    def connect(self):
        try:
            self.conn = pyodbc.connect(self.config.get_connection_string())
            print("Connection successful!")
        except pyodbc.Error as e:
            print("Error in connection:", e)

    def execute_query(self, query):
        if not self.conn:
            print("No active database connection.")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except pyodbc.Error as e:
            print("Query execution failed:", e)

    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection closed.")

