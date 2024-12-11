from Repos.bookingRepo import BookingRepository

class GetAllBookingsOfUserUseCase:
    def __init__(self):
        self.booking_repository = BookingRepository()
        pass

    def execute(self, user_id: int):
        
        try:
            return self.booking_repository.find_all_from_user(user_id)
        except ValueError as e:
            raise e("No booking with this id found")
        except Exception as e:
            print(f"Unexpected error: {e}")