from Infrastructure.API.DbConfig import SessionLocal
from Infrastructure.Domain.Entities.User import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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