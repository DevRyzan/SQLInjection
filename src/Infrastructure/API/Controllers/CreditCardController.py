from fastapi import APIRouter, HTTPException
from Repos.CreditCardRepo import CreditCardRepository

credit_card_repo = CreditCardRepository()
router = APIRouter()


@router.post("/secure")
def create_credit_card(user_id: int, credit_card_number: str, name_on_card: str, expr_date: str, cvv: int):
    card = credit_card_repo.create_credit_card(user_id, credit_card_number, name_on_card, expr_date, cvv)
    if not card:
        raise HTTPException(status_code=500, detail="Failed to create credit card")
    return {"message": "Credit card created successfully", "card_id": card["id"]}


@router.get("/secure/{card_id}")
def get_credit_card(card_id: int):
    card = credit_card_repo.get_credit_card_info(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Credit card not found")
    return {
        "id": card[0],
        "user_id": card[1],
        "credit_card_number": card[2],
        "name_on_card": card[3],
        "expr_date": card[4],
        "cvv": card[5],
    }