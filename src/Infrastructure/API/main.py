import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.append(project_root)

from Infrastructure.API.DbConfig import engine, Base
from Infrastructure.Application.DbContext import DbContext

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tables created!")

    db = DbContext()
    db.add_user(username="testuser", email="testuser@example.com")