import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import sqlite3

from Domain.Models.DTOs.PaymentDTOs.paymentInfoDTO import PaymentInfoDTO

class InSecurePaymentRepository:

    def __init__(self, db_name="sql_injection.db"):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.create_table_if_not_exists()
    
    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            address TEXT NOT NULL,
            credit_card_info_id INTEGER NOT NULL,
            payment_type TEXT NOT NULL,
            status INTEGER NOT NULL,
            amount NUMERIC(10,2) NOT NULL,
        );
        """
        self.cursor.execute(query)
        self.connection.commit()

    def create(self, credit_card_id: int, payment_info: PaymentInfoDTO):

        query = f""" INSERT INTO payments (user_id, first_name, last_name, address,credit_card_info_id, payment_type, status, amount) VALUES ('{payment_info.user_id}', '{payment_info.first_name}', '{payment_info.last_name}', '{payment_info.address}', '{payment_info.credit_card_info_id}', '{payment_info.payment_type}', '1', '{payment_info.amount}') """
        try:
            self.cursor.execute(query)
            self.connection.commit()
            id = self.cursor.lastrowid
            return {
                "id": id,
                "user_id": payment_info.user_id,
                "amount": payment_info.amount
            }
        except Exception as e:
            print(f"SQL Execution Error: {e}")
        return None