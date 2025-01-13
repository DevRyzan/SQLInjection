import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from fastapi import APIRouter, HTTPException, Request
from InSecureRepos.InSecureUserRepo import UserRepositoryInsecure
from starlette.middleware.sessions import SessionMiddleware

repo_insecure = UserRepositoryInsecure()
router = APIRouter()


@router.post("/insecure_register")
def register_user(username: str, fullname: str, email: str, password: str, request: Request):
    existing_user = repo_insecure.get_user_by_username_and_email(username, email=email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    user = repo_insecure.create_user(username=username, fullname=fullname, email=email, password=password)
    if not user:
        raise HTTPException(status_code=500, detail="Failed or sessions to register user")

    request.session['user'] = {
        "id": user["id"],
        "username": user["username"],
        "email": user["email"],
    }
    return {
        "message": "User registered successfully",
        "user_id": user["id"],
        "username": user["username"],
    }





@router.post("/insecure_login")
def login_user(username: str, password: str, request: Request):
    result = repo_insecure.insecure_login(username, password)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    request.session['user'] = {
        "id": result[0],
        "username": result[1],
        "email": result[2],
    }
    return {"message": "Login successful", "user_id": result[0], "username": result[1]}

@router.get("/insecure_users_list")
def get_all_users():
    users = repo_insecure.get_all_users()
    if not users:
        return {"message": "No users found"}
    return {"users": users}

@router.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    user = repo_insecure.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user[0], "username": user[1], "email": user[2]}

@router.put("/users/{user_id}")
def update_user(user_id: int, username: str, email: str, password: str):
    updated = repo_insecure.update_user(user_id, username=username, email=email, password=password)
    if not updated:
        raise HTTPException(status_code=400, detail="Failed to update user or no fields to update")
    return {"message": f"User with ID {user_id} updated successfully"}

@router.delete("/users/{user_id}")
def soft_delete_user(user_id: int):
    deleted = repo_insecure.soft_delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=400, detail="Failed to delete user")
    return {"message": f"User with ID {user_id} soft deleted"}