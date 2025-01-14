# from enum import Enum
# from decimal import Decimal

# class PaymentInfo:
#     class PaymentType(Enum):
#         CREDIT_CARD = 'Credit Card'
#         DEBIT_CARD = 'Debit Card'
#         CASH = 'Cash'
#         PAYPAL = 'PayPal'
#         BANK_TRANSFER = 'Bank Transfer'

#     class PaymentStatus(Enum):
#         DECLINED = 0
#         IN_PROGRESS = 1
#         NOT_ENOUGH_FUNDS = 2
#         EXPIRED_CARD = 3
#         ACCEPTED = 4

#     def __init__(self, id: int, user_id: int, first_name: str, last_name: str, address: str, credit_card_info_id: None|int, payment_type: PaymentType, status: None|PaymentStatus, amount: Decimal):
#         self.id = id
#         self.user_id = user_id
#         # Not to be confused with the name on credit card
#         # Also the person paying doesn't have to be same person as user
#         # Think about this name for invoicing purposes
#         self.first_name = first_name
#         self.last_name = last_name
#         self.address = address
#         self.credit_card_info_id = credit_card_info_id
#         self.payment_type = payment_type
#         # Status is saved to DB as '1'
#         self.status = 1,
#         self.amount = amount

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from sqlalchemy import Column, Integer, String, Boolean, Double
from API.DbConfig import Base
from sqlalchemy.ext.declarative import declarative_base

#User Entity class. We will store our property and some hidden data in this class and add new properties.
#This comment is for Bora I have changed some code in this class because it didn't fit in our db. After seeing this we can continue.

Base = declarative_base()

class PaymentInfo(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    first_name = Column(String(255)) 
    last_name = Column(String(255))
    address = Column(String(255))
    credit_card_info_id = Column(Integer)
    payment_type = Column(String(255))
    status = Column(Integer)
    amount = Column(Double)