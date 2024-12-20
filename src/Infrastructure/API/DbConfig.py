from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DB ConenctionString please check your db configuration and update here
#I will try to hold this db published on my local docker so you can connect same DB . I will update here.
DATABASE_URL = "mysql+mysqlconnector://root:Hy1aj16@localhost:3306/localmysqldb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()