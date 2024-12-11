from Domain.Models.DTOs.PaymentDTOs.creditCardInfoDTO import CreditCardInfoDTO

class PaymentRepository:

    def __init__(self):
        pass

    def create(self, credit_card_info: CreditCardInfoDTO):
        #TODO: Save to database here
        return True