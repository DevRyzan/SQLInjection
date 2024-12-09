from Domain.Entitites.User import User
from Domain.Models.DTOs.UserDTOs.RegisterDTO import RegisterDTO

class UserRepository:
    def __init__(self):
        pass

    def create(self, user: RegisterDTO):
        #TODO: Save to database here
        return True

    def find_by_id(self, user_id: int):
        
        # Psuedo Code
        # user = dbconn.find.users.where("id = user_id")
        # return user

        return None # TODO: DELME

    def find_by_email(self, email: str):
        
        # Psuedo Code
        # user = dbconn.find.users.where("email = email")
        # return user

        return None # TODO: DELME

    def exists_by_email(self, email: str):
        return self.find_by_email(email) is not None

    def delete_by_id(self, user_id: int):
        return self.users.pop(user_id, None)

    def find_all(self):
        return list(self.users.values())
