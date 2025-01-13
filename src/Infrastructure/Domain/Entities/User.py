import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from sqlalchemy import Column, Integer, String, Boolean
from API.DbConfig import Base
from sqlalchemy.ext.declarative import declarative_base

#User Entity class. We will store our property and some hidden data in this class and add new properties.
#This comment is for Bora I have changed some code in this class because it didn't fit in our db. After seeing this we can continue.

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=False, nullable=True)  
    fullname = Column(String(255), unique=False, nullable=True) 
    email = Column(String(255), unique=False, nullable=True)  
    password = Column(String(255), nullable=True)
    isDeleted = Column(Boolean, default=True)
