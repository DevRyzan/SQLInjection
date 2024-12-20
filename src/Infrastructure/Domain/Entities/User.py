from sqlalchemy import Column, Integer, String
from Infrastructure.API.DbConfig import Base

#User Entity class. We will store our property and some hidden data in this class and add new properties.
#This comment is for Bora I have changed some code in this class because it didn't fit in our db. After seeing this we can continue.
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)


# import datetime
# class User:
#     def __init__(self, id: int, firstname: str, lastname: str, birthdate: datetime.date, email: str, country: str, phonenumber: str, password: str):
#         self.id = id
#         self.firstname = firstname
#         self.lastname = lastname
#         self.birthdate = birthdate
#         self.email = email
#         self.country = country
#         self.phonenumber = phonenumber
#         self.password = password
