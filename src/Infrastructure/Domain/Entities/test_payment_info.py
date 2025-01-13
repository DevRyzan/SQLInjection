import unittest
from src.Infrastructure.Domain.Entities.PaymentInfo import PaymentInfo

#python3 -m unittest src/Infrastructure/Domain/Entities/test_payment_info.py


class TestPaymentInfo(unittest.TestCase):

    def test_payment_info_initialization(self):
        """Tests whether the PaymentInfo object is created correctly."""
        payment = PaymentInfo(
            id=1,
            user_id=101,
            first_name="John",
            last_name="Doe",
            address="123 Main Street",
            credit_card_info_id=202,
            type=PaymentInfo.PaymentType.CREDIT_CARD,
            status=PaymentInfo.PaymentStatus.IN_PROGRESS
        )

        # Check if properties are assigned correctly
        self.assertEqual(payment.id, 1)
        self.assertEqual(payment.user_id, 101)
        self.assertEqual(payment.first_name, "John")
        self.assertEqual(payment.last_name, "Doe")
        self.assertEqual(payment.address, "123 Main Street")
        self.assertEqual(payment.credit_card_info_id, 202)
        self.assertEqual(payment.type, PaymentInfo.PaymentType.CREDIT_CARD)
        self.assertEqual(payment.status, PaymentInfo.PaymentStatus.IN_PROGRESS)

    def test_payment_info_without_credit_card(self):
        """Tests the Payment Info object for cash payment without a credit card."""
        payment = PaymentInfo(
            id=2,
            user_id=102,
            first_name="Jane",
            last_name="Smith",
            address="456 Elm Street",
            credit_card_info_id=None,
            type=PaymentInfo.PaymentType.CASH,
            status=PaymentInfo.PaymentStatus.ACCEPTED
        )

        # Check if properties are assigned correctly
        self.assertEqual(payment.credit_card_info_id, None)
        self.assertEqual(payment.type, PaymentInfo.PaymentType.CASH)
        self.assertEqual(payment.status, PaymentInfo.PaymentStatus.ACCEPTED)

    def test_invalid_payment_type(self):
        """Expects a ValueError to be thrown for an invalid PaymentType."""
        with self.assertRaises(ValueError):
            PaymentInfo(
                id=3,
                user_id=103,
                first_name="Alice",
                last_name="Brown",
                address="789 Oak Avenue",
                credit_card_info_id=None,
                type="InvalidType",  # Invalid payment type
                status=PaymentInfo.PaymentStatus.DECLINED
            )

    def test_invalid_payment_status(self):
        """Expects a ValueError to be thrown for an invalid PaymentStatus."""
        with self.assertRaises(ValueError):
            PaymentInfo(
                id=4,
                user_id=104,
                first_name="Eve",
                last_name="White",
                address="987 Maple Lane",
                credit_card_info_id=None,
                type=PaymentInfo.PaymentType.BANK_TRANSFER,
                status=99  # Invalid payment status
            )


if __name__ == '__main__':
    unittest.main()
