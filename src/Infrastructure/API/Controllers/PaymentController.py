import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from decimal import Decimal
from fastapi import APIRouter, HTTPException
from Infrastructure.API.Repos.PaymentRepository  import PaymentRepository
# from Infrastructure.Domain.Models.DTOs.PaymentDTOs.creditCardInfoDTO import CreditCardInfoDTO
# from Infrastructure.Domain.Models.DTOs.PaymentDTOs.paymentInfoDTO import PaymentInfoDTO
from Infrastructure.Domain.Entities.PaymentInfo import PaymentInfo

router = APIRouter()

@router.post("/pay")
# def pay(payment_info: PaymentInfo):
def pay(user_id: int, first_name: str, last_name: str, address: str, credit_card_info_id: int, payment_type: str, status: int, amount: Decimal):
    payment_repo = PaymentRepository()

    # if not credit_card_info.user_id:
    #     raise ValueError("User id is required.")
    # if not credit_card_info.credit_card_number:
    #     raise ValueError("Credit card number is required.")
    # if not credit_card_info.name_on_card:
    #     raise ValueError("Name on card is required.")
    # if not credit_card_info.expr_date:
    #     raise ValueError("Expiration date is required.")
    # if not credit_card_info.cvv:
    #     raise ValueError("Cvv is required.")
        
    return payment_repo.create(user_id, first_name, last_name, address, credit_card_info_id, payment_type, status, amount)
    # return payment_repo.create(payment_info)