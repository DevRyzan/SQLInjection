import sqlite3


class CreditCardRepository:
    def __init__(self, db_name="sql_injection.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS credit_card_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            credit_card_number TEXT NOT NULL,
            name_on_card TEXT NOT NULL,
            expr_date TEXT NOT NULL,
            cvv INTEGER NOT NULL
        );
        """
        self.cursor.execute(query)
        self.connection.commit()

    def create_credit_card(self, user_id, credit_card_number, name_on_card, expr_date, cvv):
        query = f"""INSERT INTO credit_card_info (user_id, credit_card_number, name_on_card, expr_date, cvv)
                    VALUES ('{user_id}', '{credit_card_number}', '{name_on_card}', '{expr_date}', '{cvv}')"""
        try:
            self.cursor.execute(query)
            self.connection.commit()
            id = self.cursor.lastrowid
            return {"id": id, "user_id": user_id, "name_on_card": name_on_card}
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return None

    def get_credit_card_info(self, card_id):
        query = f"SELECT * FROM credit_card_info WHERE id = {card_id}"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            print(f"Credit Card Info: {result}")
            return result
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return None