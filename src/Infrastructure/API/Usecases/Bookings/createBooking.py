from Repos.bookingRepo import BookingRepository
from Domain.Models.DTOs.BookingDTOs.CreateBookingDTO import CreateBookingDTO

class CreateBookingUseCase:
    def __init__(self):
        self.booking_repo = BookingRepository()

    def execute(self, booking_data: CreateBookingDTO):
        if not booking_data.start_date:
            raise ValueError("Start date is required.")
        if not booking_data.end_date:
            raise ValueError("End date is required.")
        if not booking_data.user_id:
            raise ValueError("User id is required.")
        return self.booking_repo.create(booking_data)