from enum import Enum

class PaymentInfo:
    class PaymentType(Enum):
        CREDIT_CARD = 'Credit Card'
        DEBIT_CARD = 'Debit Card'
        CASH = 'Cash'
        PAYPAL = 'PayPal'
        BANK_TRANSFER = 'Bank Transfer'

    class PaymentStatus(Enum):
        DECLINED = 0
        IN_PROGRESS = 1
        NOT_ENOUGH_FUNDS = 2
        EXPIRED_CARD = 3
        ACCEPTED = 4

    def __init__(self, id: int, user_id: int, first_name: str, last_name: str, address: str, credit_card_info_id: None|int, type: PaymentType, status: PaymentStatus):
        self.id = id
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.credit_card_info_id = credit_card_info_id
        self.type = type
        self.status = status