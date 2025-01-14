from fastapi import APIRouter, HTTPException
from InSecureRepos.InSecurePaymentRepo import PaymentRepository

payment_repo = PaymentRepository()
router = APIRouter()


@router.post("/payments")
def create_payment_info(user_id: int, first_name: str, last_name: str, address: str, credit_card_info_id: int, type: str, status: int):
    payment = payment_repo.create_payment_info(user_id, first_name, last_name, address, credit_card_info_id, type, status)
    if not payment:
        raise HTTPException(status_code=500, detail="Failed to create payment info")
    return {"message": "Payment info created successfully", "payment_id": payment["id"]}


@router.get("/payments/{payment_id}")
def get_payment_info(payment_id: int):
    payment = payment_repo.get_payment_info(payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment info not found")
    return {
        "id": payment[0],
        "user_id": payment[1],
        "first_name": payment[2],
        "last_name": payment[3],
        "address": payment[4],
        "credit_card_info_id": payment[5],
        "type": payment[6],
        "status": payment[7],
    }


@router.put("/payments/{payment_id}")
def update_payment_status(payment_id: int, status: int):
    updated = payment_repo.update_payment_status(payment_id, status)
    if not updated:
        raise HTTPException(status_code=400, detail="Failed to update payment status")
    return {"message": f"Payment status updated successfully for payment ID {payment_id}"}