import unittest
import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from Infrastructure.Domain.Entities.Booking import Booking

#python3 -m unittest src/Infrastructure/Domain/Entities/test_booking.py

class TestBooking(unittest.TestCase):
    def test_booking_initialization(self):
        # sample data
        booking_id = 1
        start_date = datetime.date(2025, 1, 1)
        end_date = datetime.date(2025, 1, 5)
        user_id = 101
        payment_info_id = 202

        # creating the booking object
        booking = Booking(booking_id, start_date, end_date, user_id, payment_info_id)

        # check if values ​​are assigned correctly
        self.assertEqual(booking.id, booking_id)
        self.assertEqual(booking.start_date, start_date)
        self.assertEqual(booking.end_date, end_date)
        self.assertEqual(booking.user_id, user_id)
        self.assertEqual(booking.payment_info_id, payment_info_id)

    def test_booking_without_payment(self):
        # Creating a Booking object without Payment info ID
        booking_id = 2
        start_date = datetime.date(2025, 2, 1)
        end_date = datetime.date(2025, 2, 3)
        user_id = 102
        payment_info_id = None  # no payment info

        booking = Booking(booking_id, start_date, end_date, user_id, payment_info_id)

        # Check Payment info as None
        self.assertIsNone(booking.payment_info_id)

if __name__ == '__main__':
    unittest.main()
