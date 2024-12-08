from Domain.Entitites.User import User
from Domain.Models.DTOs.RegisterDTO import RegisterDTO

class UserRepository:
    def __init__(self):
        self.users = {}  # In-memory storage (dictionary with user ID as key)

    def create(self, user: RegisterDTO):
        # Save to database here
        return True

    def find_by_id(self, user_id: int):
        return self.users.get(user_id)

    def find_by_email(self, email: str):
        return next((user for user in self.users.values() if user.email == email), None)

    def exists_by_email(self, email: str):
        return self.find_by_email(email) is not None

    def delete_by_id(self, user_id: int):
        return self.users.pop(user_id, None)

    def find_all(self):
        return list(self.users.values())
