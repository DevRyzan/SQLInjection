import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import sqlite3

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
# from DbConfig import SessionLocal

# from Domain.Models.DTOs.PaymentDTOs.paymentInfoDTO import PaymentInfoDTO
from Domain.Entities.PaymentInfo import PaymentInfo
from decimal import Decimal

#TODO: revisit these
engine = create_engine('sqlite:///sql_injection.db')  # Replace with your database path
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

class PaymentRepository:

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
            amount NUMERIC(10,2) NOT NULL
        )
        """
        self.cursor.execute(query)
        self.connection.commit()

    def create(user_id: int, first_name: str, last_name: str, address: str, credit_card_info_id: int, payment_type: str, status: int, amount: Decimal, self):

        # try:
        #     self.cursor.execute('INSERT INTO payments (user_id, first_name, last_name, address,credit_card_info_id, payment_type, status, amount) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (payment_info.user_id, payment_info.first_name, payment_info.last_name, payment_info.address, payment_info.credit_card_info_id, payment_info.payment_type, 1, payment_info.amount))

        #     self.connection.commit()
        #     id = self.cursor.lastrowid
        #     return {
        #         "id": id,
        #         "user_id": payment_info.user_id,
        #         "amount": payment_info.amount
        #     }
        # except Exception as e:
        #     print(f"SQL Execution Error: {e}")
        # return None


        new_payment = PaymentInfo(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            address=address,
            credit_card_info_id=credit_card_info_id,
            payment_type=payment_type,
            status=1,  # Default status
            amount=amount
        )
        # new_payment = Pay
        #     "user_id": user_id,
        #     "first_name": first_name,
        #     "last_name": last_name,
        #     "address": address,
        #     "credit_card_info_id": credit_card_info_id,
        #     "payment_type": payment_type,
        #     "status": 1,  # Assuming 1 is the default for active or similar
        #     "amount": amount
        
                    
        
        session.add(new_payment)
        session.commit()