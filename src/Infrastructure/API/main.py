import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from DbConfig import engine, Base
from Application.DbContext import DbContext

#Create MetaData on MySQL DB
def create_tables():
    try:
        print("📦 Tables Are Creating...")
        Base.metadata.create_all(bind=engine)
        print("✅ Tables Created.")
    except Exception as e:
        print(f"❌ Error creating {e}")

#Seed Data for beging 
def seed_users():
    db = DbContext()
    print("🌱 Seed Data User Working...")

    users = [
        {"username": "admin", "email": "admin@example.com"},
        {"username": "user1", "email": "user1@example.com"},
        {"username": "user2", "email": "user2@example.com"},
    ]

    for user in users:
        db.add_user(user["username"], user["email"])

    print("✅ Seed Data Added!")


if __name__ == "__main__":
    create_tables()
    seed_users()