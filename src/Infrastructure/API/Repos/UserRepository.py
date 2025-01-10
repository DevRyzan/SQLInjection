import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from  DbConfig import SessionLocal
from  Domain.Entities.User import User

class UserRepository:
    def __init__(self):
        self.session = SessionLocal()

    def get_user_by_username(self, username):
        return self.session.query(User).filter(User.username == username, User.isDeleted == False).first()

    def create_user(self, username, email, password):
        new_user = User(username=username, email=email, password=password)
        new_user.isDeleted = False
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_user_by_id(self, user_id):
        return self.session.query(User).filter(User.id == user_id, User.isDeleted == False).first()

    def soft_delete_user(self, user_id):
        user = self.session.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        user.isDeleted = True
        self.session.commit()
        return True