import sqlite3

class UserRepo:
    def __init__(self, db_name="sql_injection.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            fullname TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            isDeleted BOOLEAN DEFAULT 0
        );
        """
        self.cursor.execute(query)
        self.connection.commit()

    def recreate_users_table(self):
        try:
            self.cursor.execute("ALTER TABLE users RENAME TO users_old;")

            self.cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                fullname TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                isDeleted BOOLEAN DEFAULT 0
            );
            """)

            self.cursor.execute("""
            INSERT INTO users (id, username, fullname ,email, password, isDeleted)
            SELECT id, username, email, password, isDeleted FROM users_old;
            """)

            self.cursor.execute("DROP TABLE users_old;")
            self.connection.commit()
            print("Users table successfully recreated with updated schema.")
        except Exception as e:
            print(f"Error recreating users table: {e}")

    def create_user(self, username, fullname, email, password):
        query = """INSERT INTO users (username, fullname, email, password, isDeleted) 
           VALUES (?, ?, ?, ?, 0)"""

        try:
            self.cursor.execute(query, (username, fullname, email, password))
            self.connection.commit()
            id = self.cursor.lastrowid
            return {
                "id": id,
                "username": username,
                "email": email,
            }
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return None
    

    def insecure_login(self, username: str, password: str): 
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        try:
            self.cursor.execute(query, (username, password)) 
            result = self.cursor.fetchone()   
            return result  
        except Exception as e:
            print(f"SQL Execution Error: {e}")   
        return None  
    
    def get_all_users(self):
        query = "SELECT * FROM users WHERE isDeleted = 0"
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            print(f"All Users: {results}")
            return results
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return []
    
    def get_user_by_id(self, user_id: int):
        query = "SELECT * FROM users WHERE id = ? AND isDeleted = 0"
        try:
            self.cursor.execute(query, (user_id,))
            result = self.cursor.fetchone()
            print(f"User by ID {user_id}: {result}")
            return result
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return None
    
    def get_user_by_username_and_email(self, user_name: str, email : str):
        query = "SELECT * FROM users WHERE username = ? OR email = ? AND isDeleted = 0"
        try:
            self.cursor.execute(query, (user_name, email))
            result = self.cursor.fetchone()
            print(f"User by username {user_name}: {result}")
            return result
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return None
    
    def update_user(self, user_id: int, username=None, email=None, password=None):
        
        fields_to_update = []
        params = []

        if username:
            fields_to_update.append("username = ?")
            params.append(username)

        if email:
            fields_to_update.append("email = ?")
            params.append(email)

        if password:
            fields_to_update.append("password = ?")
            params.append(password)

        if not fields_to_update:
            print("No fields to update")
            return False

        query = f"UPDATE users SET {', '.join(fields_to_update)} WHERE id = ? AND isDeleted = 0"
        params.append(user_id)  # Add `user_id` to the parameters

        try:
            self.cursor.execute(query, params)  # Pass `params` directly
            self.connection.commit()
            print(f"User with ID {user_id} updated successfully")
            return True
        except Exception as e:
            print(f"SQL Execution Error: {e}")
            return False


    def soft_delete_user(self, user_id: int):
        query = "UPDATE users SET isDeleted = 1 WHERE id = ?"
        try:
            self.cursor.execute(query, (user_id,))
            self.connection.commit()
            print(f"User with ID {user_id} soft deleted")
            return True
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return False