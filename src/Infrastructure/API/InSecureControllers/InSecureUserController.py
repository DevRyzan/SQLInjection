import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from fastapi import APIRouter, HTTPException, FastAPI
from InSecureRepos.InSecureUserRepo import UserRepositoryInsecure

router = APIRouter()
repo_insecure = UserRepositoryInsecure()
app= FastAPI()

@app.post("/register")
def register_insecure(username: str, email: str, password: str):
    repo_insecure.create_user(username=username, email=email, password=password)
    return {"message": "User registered successfully", "username": username}

@app.get("/{user_id}")
def get_user_insecure(user_id: int):
    user = repo_insecure.get_user_by_id(user_id)
    if not user:
        return {"error": f"User with ID {user_id} not found"}
    return {"id": user[0], "username": user[1], "email": user[2]}

@app.post("/login")
def insecure_login(username: str, password: str):
    result = repo_insecure.insecure_login(username, password)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Login successful", "user_id": result[0], "username": result[1]} 