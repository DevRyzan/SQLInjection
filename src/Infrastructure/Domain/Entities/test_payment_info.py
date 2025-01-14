import unittest
from src.Infrastructure.Domain.Entities.PaymentInfo import PaymentInfo

#python3 -m unittest src/Infrastructure/Domain/Entities/test_payment_info.py

class TestPaymentInfo(unittest.TestCase):

    def test_payment_info_initialization(self):
        # tests whether the PaymentInfo object is created correctly
        payment = PaymentInfo(
            id=1,
            user_id=101,
            first_name="Sadik Emre",
            last_name="Ikiz",
            address="Antalya",
            credit_card_info_id=202,
            type=PaymentInfo.PaymentType.CREDIT_CARD,
            status=PaymentInfo.PaymentStatus.IN_PROGRESS
        )

        # check if properties are assigned correctly
        self.assertEqual(payment.id, 1)
        self.assertEqual(payment.user_id, 101)
        self.assertEqual(payment.first_name, "Sadik Emre")
        self.assertEqual(payment.last_name, "Ikiz")
        self.assertEqual(payment.address, "Antalya")
        self.assertEqual(payment.credit_card_info_id, 202)
        self.assertEqual(payment.type, PaymentInfo.PaymentType.CREDIT_CARD)
        self.assertEqual(payment.status, PaymentInfo.PaymentStatus.IN_PROGRESS)

    def test_payment_info_without_credit_card(self):
        # tests the Payment Info object for cash payment without a credit card
        payment = PaymentInfo(
            id=2,
            user_id=102,
            first_name="Sadik Emre",
            last_name="Ikiz",
            address="Antalya",
            credit_card_info_id=None,
            type=PaymentInfo.PaymentType.CASH,
            status=PaymentInfo.PaymentStatus.ACCEPTED
        )

        # check if properties are assigned correctly
        self.assertEqual(payment.credit_card_info_id, None)
        self.assertEqual(payment.type, PaymentInfo.PaymentType.CASH)
        self.assertEqual(payment.status, PaymentInfo.PaymentStatus.ACCEPTED)

    def test_invalid_payment_type(self):
        # tests what happens when an invalid PaymentType is used
        payment = PaymentInfo(
            id=3,
            user_id=103,
            first_name="Sadik Emre",
            last_name="Ikiz",
            address="Antalya",
            credit_card_info_id=None,
            type="InvalidType",  # Invalid payment type
            status=PaymentInfo.PaymentStatus.DECLINED
        )

        # check if the invalid type is assigned as is
        self.assertEqual(payment.type, "InvalidType")

    def test_invalid_payment_status(self):
        # tests what happens when an invalid PaymentStatus is used.
        payment = PaymentInfo(
            id=4,
            user_id=104,
            first_name="Sadik Emre",
            last_name="Ikiz",
            address="Antalya",
            credit_card_info_id=None,
            type=PaymentInfo.PaymentType.BANK_TRANSFER,
            status=99  # invalid payment status
        )

        # check if the invalid status is assigned as is
        self.assertEqual(payment.status, 99)

if __name__ == '__main__':
    unittest.main()

