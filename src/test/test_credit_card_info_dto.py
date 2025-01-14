import unittest
import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from Infrastructure.Domain.Models.DTOs.PaymentDTOs.creditCardInfoDTO import CreditCardInfoDTO

#python3 -m unittest src/Infrastructure/Domain/Models/DTOs/PaymentDTOs/test_credit_card_info_dto.py


class TestCreditCardInfoDTO(unittest.TestCase):

    def test_credit_card_info_dto_initialization(self):
        # tests whether the CreditCardInfoDTO object is created correctly
        user_id = 101
        credit_card_number = "1234567890123456"
        name_on_card = "Sadik Emre Ikiz"
        expr_date = datetime.date(2025, 12, 31)
        cvv = "123"

        # create DTO object
        card_info_dto = CreditCardInfoDTO(
            user_id=user_id,
            credit_card_number=credit_card_number,
            name_on_card=name_on_card,
            expr_date=expr_date,
            cvv=cvv
        )

        # check if values ​​are assigned correctly
        self.assertEqual(card_info_dto.user_id, user_id)
        self.assertEqual(card_info_dto.credit_card_number, credit_card_number)
        self.assertEqual(card_info_dto.name_on_card, name_on_card)
        self.assertEqual(card_info_dto.expr_date, expr_date)
        self.assertEqual(card_info_dto.cvv, cvv)

    def test_invalid_credit_card_number(self):
        # tests creating a CreditCardInfoDTO with an invalid credit card number
        user_id = 101
        credit_card_number = "1234"  # invalid credit card number
        name_on_card = "Sadik Emre Ikiz"
        expr_date = datetime.date(2025, 12, 31)
        cvv = "123"

        with self.assertRaises(ValueError):
            CreditCardInfoDTO(
                user_id=user_id,
                credit_card_number=credit_card_number,
                name_on_card=name_on_card,
                expr_date=expr_date,
                cvv=cvv
            )

    def test_expired_card(self):
        # tests creating a DTO with an expired credit card
        user_id = 101
        credit_card_number = "1234567890123456"
        name_on_card = "Sadik Emre Ikiz"
        expr_date = datetime.date(2020, 12, 31)  # expired date
        cvv = "123"

        with self.assertRaises(ValueError):
            CreditCardInfoDTO(
                user_id=user_id,
                credit_card_number=credit_card_number,
                name_on_card=name_on_card,
                expr_date=expr_date,
                cvv=cvv
            )


if __name__ == "__main__":
    unittest.main()
