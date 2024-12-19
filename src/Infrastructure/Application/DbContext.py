from Infrastructure.API.DbConfig import SessionLocal
from Infrastructure.Domain.Entities.User import User


class DbContext:
    def __init__(self):
        self.session = SessionLocal()
#Seed data for User DB 
    def add_user(self, username, email):
        new_user = User(username=username, email=email)
        self.session.add(new_user)
        self.session.commit()
        print(f"User created: {username}")