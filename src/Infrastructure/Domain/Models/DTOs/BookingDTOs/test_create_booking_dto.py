import unittest
import datetime
from src.Infrastructure.Domain.Models.DTOs.BookingDTOs.CreateBookingDTO import CreateBookingDTO

#python3 -m unittest src/Infrastructure/Domain/Models/DTOs/BookingDTOs/test_create_booking_dto.py


class TestCreateBookingDTO(unittest.TestCase):

    def test_create_booking_dto_initialization(self):
        #Tests whether the CreateBookingDTO object has been created correctly
        # Valid input values
        start_date = datetime.date(2025, 1, 1)
        end_date = datetime.date(2025, 1, 10)
        user_id = 101

        # Create DTO object
        booking_dto = CreateBookingDTO(start_date=start_date, end_date=end_date, user_id=user_id)

        # Check if values ​​are assigned correctly
        self.assertEqual(booking_dto.start_date, start_date)
        self.assertEqual(booking_dto.end_date, end_date)
        self.assertEqual(booking_dto.user_id, user_id)

    def test_invalid_dates(self):
        #Tests creating CreateBookingDTO with an invalid date range
        # Invalid date range
        start_date = datetime.date(2025, 1, 10)
        end_date = datetime.date(2025, 1, 1)  # Start date after end date
        user_id = 101

        # Expect ValueError to be thrown in incorrect date range
        with self.assertRaises(ValueError):
            CreateBookingDTO(start_date=start_date, end_date=end_date, user_id=user_id)

    def test_missing_user_id(self):
        #Tests creating CreateBookingDTO with a missing user ID
        start_date = datetime.date(2025, 1, 1)
        end_date = datetime.date(2025, 1, 10)
        user_id = None  # Missing user ID

        with self.assertRaises(TypeError):
            CreateBookingDTO(start_date=start_date, end_date=end_date, user_id=user_id)


if __name__ == "__main__":
    unittest.main()
