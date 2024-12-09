from Domain.Models.DTOs.UserDTOs.RegisterDTO import RegisterDTO
from Repos.userRepo import UserRepository

class CreateUserUseCase:
    def __init__(self):
        self.user_repository = UserRepository() #creates a new UserRepo object, there is no need to use 'new' (doesn't exist in python anyway)

    def execute(self, user_data: RegisterDTO):
        if not user_data.email or not user_data.password:
            raise ValueError("Email and password are required.")
        if self.user_repository.exists_by_email(user_data.email):
            raise ValueError("User with this email already exists.")
        return self.user_repository.create(user_data)
