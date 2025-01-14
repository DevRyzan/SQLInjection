import unittest
import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from Infrastructure.Domain.Models.DTOs.BookingDTOs.CreateBookingDTO import CreateBookingDTO

#python3 -m unittest src/Infrastructure/Domain/Models/DTOs/BookingDTOs/test_create_booking_dto.py


class TestCreateBookingDTO(unittest.TestCase):

    def test_create_booking_dto_initialization(self):
        # tests whether the CreateBookingDTO object has been created correctly
        # valid input values
        start_date = datetime.date(2025, 1, 1)
        end_date = datetime.date(2025, 1, 10)
        user_id = 101

        # create DTO object
        booking_dto = CreateBookingDTO(start_date=start_date, end_date=end_date, user_id=user_id)

        # check if values ​​are assigned correctly
        self.assertEqual(booking_dto.start_date, start_date)
        self.assertEqual(booking_dto.end_date, end_date)
        self.assertEqual(booking_dto.user_id, user_id)

    def test_invalid_dates(self):
        # tests creating CreateBookingDTO with an invalid date range
        # invalid date range
        start_date = datetime.date(2025, 1, 10)
        end_date = datetime.date(2025, 1, 1)  # start date after end date
        user_id = 101

        # expect ValueError to be thrown in incorrect date range
        with self.assertRaises(ValueError):
            CreateBookingDTO(start_date=start_date, end_date=end_date, user_id=user_id)

    def test_missing_user_id(self):
        # tests creating CreateBookingDTO with a missing user ID
        start_date = datetime.date(2025, 1, 1)
        end_date = datetime.date(2025, 1, 10)
        user_id = None  # missing user ID

        with self.assertRaises(TypeError):
            CreateBookingDTO(start_date=start_date, end_date=end_date, user_id=user_id)


if __name__ == "__main__":
    unittest.main()
