import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from fastapi import FastAPI
from Controller.UserController import router as user_router
from DbConfig import engine, Base
from Application.DbContext import DbContext
from Controller import UserController


try:
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")
except Exception as e:
    print(f"Error creating tables: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# #Create MetaData on MySQL DB
# def create_tables():
#     try:xdxd
#         print("📦 Tables Are Creating...")
#         Base.metadata.create_all(bind=engine)
#         print("✅ Tables Created.")
#     except Exception as e:
#         print(f"❌ Error creating {e}")

# #Seed Data for beging 
# def seed_users():
#     db = DbContext()
#     print("🌱 Seed Data User Working...")

#     users = [
#         {"username": "admin", "email": "admin@example.com"},
#         {"username": "user1", "email": "user1@example.com"},
#         {"username": "user2", "email": "user2@example.com"},
#     ]

#     for user in users:
#         db.add_user(user["username"], user["email"])

#     print("✅ Seed Data Added!")


# if __name__ == "__main__":
#     create_tables()
#     seed_users()