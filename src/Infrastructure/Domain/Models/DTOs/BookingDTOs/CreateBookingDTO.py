import datetime

class CreateBookingDTO:
    def __init__(self, start_date: datetime.date, end_date: datetime.date, user_id: int):
        if end_date < start_date:
            raise ValueError("End date cannot be earlier than start date.")
        if user_id is None:
            raise TypeError("User ID cannot be None.")
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id