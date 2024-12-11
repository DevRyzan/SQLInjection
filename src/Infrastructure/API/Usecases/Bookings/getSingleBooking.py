from Repos.bookingRepo import BookingRepository

class GetSingleBookingUseCase:
    def __init__(self):
        self.booking_repository = BookingRepository()
        pass

    def execute(self, booking_id: int):
        
        try:
            return self.booking_repository.find_by_id(booking_id)
        except ValueError as e:
            raise e("No booking with this id found")
        except Exception as e:
            print(f"Unexpected error: {e}")