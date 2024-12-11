import datetime

class CreateBookingDTO:
    def __init__(self, start_date: datetime.date, end_date: datetime.date, user_id: int):
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id