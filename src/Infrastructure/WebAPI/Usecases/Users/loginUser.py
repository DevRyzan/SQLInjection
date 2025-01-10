from Domain.Models.DTOs.UserDTOs.LoginDTO import LoginDTO
from src.Infrastructure.WebAPI.Repos.UserRepository import UserRepository

class LoginUserUseCase:
    def __init__(self):
        self.user_repository = UserRepository() #creates a new UserRepo object, there is no need to use 'new' (doesn't exist in python anyway)

    def execute(self, user_data: LoginDTO):
        email = user_data.get("email")
        password = user_data.get("password")
        if not email or not password:
            raise ValueError("Email and password are required.")
        
        try:
            user = self.user_repository.find_by_email(email)
            # return self.user_repository.find_by_email(email) # TODO: uncomment this if user doesn't return as expected
        except ValueError as e:
            raise e("No user with this email found")
        except Exception as e:
            print(f"Unexpected error: {e}")
        else:
            if user_data.password != user.password:
                raise ValueError("Wrong password")
            
        return user #TODO: check and make sure it doesnt return empty user
