import datetime

# Right now this is identical to Booking entity but this might change according to business requirements in the future
class CreateBookingDTO:
    def __init__(self, id: int, start_date: datetime.date, end_date: datetime.date, user_id: int):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id