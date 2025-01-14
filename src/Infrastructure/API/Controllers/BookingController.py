from fastapi import APIRouter, HTTPException
from Repos.BookingRepo import BookingRepository

booking_repo = BookingRepository()
router = APIRouter()


@router.post("/secure")
def create_booking(start_date: str, end_date: str, user_id: int, payment_info_id: int = None):
    booking = booking_repo.create_booking(start_date, end_date, user_id, payment_info_id)
    if not booking:
        raise HTTPException(status_code=500, detail="Failed to create booking")
    return {"message": "Booking created successfully", "booking_id": booking["id"]}


@router.get("/secure/{booking_id}")
def get_booking(booking_id: int):
    booking = booking_repo.get_booking(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {
        "id": booking[0],
        "start_date": booking[1],
        "end_date": booking[2],
        "user_id": booking[3],
        "payment_info_id": booking[4],
    }


# @router.put("/secure/{booking_id}")
# def update_booking_payment_info(booking_id: int, payment_info_id: int):
#     updated = booking_repo.update_payment_info(booking_id, payment_info_id)
#     if not updated:
#         raise HTTPException(status_code=400, detail="Failed to update payment info for booking")
#     return {"message": f"Payment info updated successfully for booking ID {booking_id}"}


# @router.delete("/{booking_id}")
# def delete_booking(booking_id: int):
#     deleted = booking_repo.delete_booking(booking_id)
#     if not deleted:
#         raise HTTPException(status_code=400, detail="Failed to delete booking")
#     return {"message": f"Booking with ID {booking_id} deleted successfully"}