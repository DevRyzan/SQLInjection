import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from fastapi import APIRouter, HTTPException
from Infrastructure.WebAPI.Repos.UserRepository import UserRepository

router = APIRouter()
repo = UserRepository()

@router.post("/register")
def register(username: str, email: str, password: str):
    repo = UserRepository()
    existing_user = repo.get_user_by_username(username)
    if existing_user:
        return {"error": "Username already exists"}

    user = repo.create_user(username=username, email=email, password=password)
    if user:   
        return {"message": "User registered successfully", "user_id": user.id}
    else:
        return {"error": "Failed to register user"}


@router.get("/{user_id}")
def get_user(user_id: int):
    user = repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"id": user.id, "username": user.username, "email": user.email}