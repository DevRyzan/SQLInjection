import sqlite3


class PaymentRepository:
    def __init__(self, db_name="sql_injection.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS payment_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            address TEXT NOT NULL,
            credit_card_info_id INTEGER,
            type TEXT NOT NULL,
            status INTEGER NOT NULL
        );
        """
        self.cursor.execute(query)
        self.connection.commit()

    def create_payment_info(self, user_id, first_name, last_name, address, credit_card_info_id, type, status):
        query = """INSERT INTO payment_info (user_id, first_name, last_name, address, credit_card_info_id, type, status)
           VALUES (?, ?, ?, ?, ?, ?, ?)"""
        
        try:
            self.cursor.execute(query, (user_id, first_name, last_name, address, credit_card_info_id, type, status))
            self.connection.commit()
            id = self.cursor.lastrowid
            return {"id": id, "user_id": user_id, "status": status}
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return None

    def get_payment_info(self, payment_id):
        query = "SELECT * FROM payment_info WHERE id = ?"
        try:
            self.cursor.execute(query, (payment_id,))
            result = self.cursor.fetchone()
            print(f"Payment Info: {result}")
            return result
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return None