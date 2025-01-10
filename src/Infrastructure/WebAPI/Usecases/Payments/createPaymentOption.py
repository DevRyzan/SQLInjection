from Repos.paymentRepo import PaymentRepository
from Domain.Models.DTOs.PaymentDTOs.creditCardInfoDTO import CreditCardInfoDTO

class CreatePaymentOptionUseCase:
    def __init__(self):
        self.payment_repo = PaymentRepository()

    def execute(self, credit_card_info: CreditCardInfoDTO):
        # if not payment_data.start_date:
        #     raise ValueError("Start date is required.")
        # if not payment_data.end_date:
        #     raise ValueError("End date is required.")
        # if not payment_data.user_id:
        #     raise ValueError("User id is required.")
        # return self.payment_repo.create(payment_data)

        if not credit_card_info.user_id:
            raise ValueError("User id is required.")
        if not credit_card_info.credit_card_number:
            raise ValueError("Credit card number is required.")
        if not credit_card_info.name_on_card:
            raise ValueError("Name on card is required.")
        if not credit_card_info.expr_date:
            raise ValueError("Expirtaion date is required.")
        if not credit_card_info.cvv:
            raise ValueError("Cvv is required.")
        
        return self.payment_repo.create(credit_card_info)