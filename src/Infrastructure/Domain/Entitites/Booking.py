import datetime

class Booking:
    def __init__(self, id: int, startdate: datetime.date, enddate: datetime.date, userid: int):
        self.id = id
        self.stardate = startdate
        self.enddate = enddate
        self.userid = userid