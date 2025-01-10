import sqlite3

class UserRepositoryInsecure:
    def __init__(self, db_name="sql_injection.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            isDeleted BOOLEAN DEFAULT 0
        );
        """
        self.cursor.execute(query)
        self.connection.commit()

    def create_user(self, username, email, password):
        query = f"INSERT INTO users (username, email, password, isDeleted) VALUES ('{username}', '{email}', '{password}', 0)"
        self.cursor.execute(query)
        self.connection.commit()

    def insecure_login(self, username: str, password: str): 
        query = f"SELECT * FROM users WHERE username = '{username}' AND (password = '{password}')"
        print(f"Generated Query: {query}")  
        try:
            self.cursor.execute(query)   
            result = self.cursor.fetchone()   
            print(f"Query Result: {result}")  
            return result  
        except Exception as e:
            print(f"SQL Execution Error: {e}")   
        return None  