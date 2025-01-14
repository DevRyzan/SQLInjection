import datetime

class CreditCardInfoDTO:
    def __init__(self, user_id: int, credit_card_number: str, name_on_card: str, expr_date: datetime.date, cvv: int):
        if len(credit_card_number) < 16:
            raise ValueError("Credit card number must be at least 16 characters long.")
        if expr_date < datetime.date.today():
            raise ValueError("Credit card has expired.")
        self.user_id = user_id
        self.credit_card_number = credit_card_number
        self.name_on_card = name_on_card
        self.expr_date = expr_date
        self.cvv = cvv