from Domain.Models.DTOs.RegisterDTO import RegisterDTO
from Repos.userRepo import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repository): #TODO: Create user repo
        self.user_repository = UserRepository()

    def execute(self, user_data: RegisterDTO):
        if not user_data.get("email") or not user_data.get("password"):
            raise ValueError("Email and password are required.")
        if self.user_repository.exists_by_email(user_data["email"]):
            raise ValueError("User with this email already exists.")
        return self.user_repository.save(user_data)
