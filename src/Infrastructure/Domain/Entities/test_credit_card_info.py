import unittest
import datetime
from src.Infrastructure.Domain.Entities.CreditCardInfo import CreditCardInfo

#python3 -m unittest src/Infrastructure/Domain/Entities/test_credit_card_info.py

class TestCreditCardInfo(unittest.TestCase):
    def test_credit_card_initialization(self):
        # sample datas
        card_id = 1
        user_id = 101
        credit_card_number = "1234567812345678"
        name_on_card = "Sadik Emre"
        expr_date = datetime.date(2025, 12, 31)
        cvv = "123"

        # creating CreditCardInfo object
        card = CreditCardInfo(card_id, user_id, credit_card_number, name_on_card, expr_date, cvv)

        # check if values ​​are assigned correctly
        self.assertEqual(card.id, card_id)
        self.assertEqual(card.user_id, user_id)
        self.assertEqual(card.credit_card_number, credit_card_number)
        self.assertEqual(card.name_on_card, name_on_card)
        self.assertEqual(card.expr_date, expr_date)
        self.assertEqual(card.cvv, cvv)

    def test_invalid_cvv(self):
        # creating a CreditCardInfo object with an incorrect CVV
        card_id = 2
        user_id = 102
        credit_card_number = "8765432187654321"
        name_on_card = "Sadik Emre"
        expr_date = datetime.date(2024, 6, 30)
        invalid_cvv = "12"  # CVV is missing (must be 3 digits)

        with self.assertRaises(ValueError):
            CreditCardInfo(card_id, user_id, credit_card_number, name_on_card, expr_date, invalid_cvv)

if __name__ == '__main__':
    unittest.main()
