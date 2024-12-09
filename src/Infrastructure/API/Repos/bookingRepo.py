from Domain.Models.DTOs.BookingDTOs.CreateBookingDTO import CreateBookingDTO

class BookingRepository:
    def __init__(self):
        pass

    def create(self, booking_data: CreateBookingDTO ):
        #TODO: Save to database here
        return True

    def find_by_id(self, booking_id: int):
        # Psuedo Code
        # user = dbconn.find.bookings.where("id = booking_id")
        # return user
        return None
    

