import datetime

from Domain.Models.DTOs.BookingDTOs.CreateBookingDTO import CreateBookingDTO

class BookingRepository:
    def __init__(self):
        pass

    def create(self, booking_data: CreateBookingDTO ):
        #TODO: Save to database here
        return True

    def find_by_id(self, booking_id: int):
        # Psuedo Code
        # booking = dbconn.find.bookings.where("id = booking_id")
        # return booking
        return None
    
    def find_all_from_user(self, user_id: int):

        # Psuedo Code
        # bookings = dbconn.find.bookings.where("user_id = {user_id}")
        # return bookings
        return None
    
    def find_between_dates(self, start_date: datetime.date, end_date: datetime.date):

        # Psuedo Code
        # bookings = dbconn.find.bookings.where("start_date > {start_date}").and("end_date < {end_date}")
        # return bookings
        return None
    
    def find_between_dates(self, user_id: int, start_date: datetime.date, end_date: datetime.date):

        # Psuedo Code
        # bookings = dbconn.find.bookings.where("user_id = {user_id}").and("start_date > {start_date}").and("end_date < {end_date}")
        # return bookings
        return None
    

