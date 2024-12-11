import datetime

# We can get the status of the booking from the status of payment?

# Making payment info id nullable because I think first the booking should be created then payed. If the booking has payment_info_id as None we can derive the status from that

# If this seems too complicated we can create virtual properties of status that doesn't exist in the model
class Booking:
    def __init__(self, id: int, start_date: datetime.date, end_date: datetime.date, user_id: int, payment_info_id: None|int):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.user_id = user_id
        self.payment_info_id = payment_info_id

        # # Example virtual property
        # if payment_info_id == None:
        #     self.status = 0 # No payment made
        # else:
        #     self.status = 1 # Payment in progress
        