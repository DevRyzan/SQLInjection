import datetime

class Booking:
    def __init__(self, id: int, start_date: datetime.date, end_date: datetime.date, userid: int):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.userid = userid