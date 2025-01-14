import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from fastapi import FastAPI
from Controllers.UserController import router as user_router
from DbConfig import engine, Base
from Application.DbContext import  DbContext
from InSecureControllers.InSecureUserController import router as router_insecure 
from InSecureRepos.InSecureUserRepo import UserRepositoryInsecure 
from starlette.middleware.sessions import SessionMiddleware

from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

try:
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")
except Exception as e:
    print(f"Error creating tables: {e}")

# db_name = "sql_injection.db"
# repo_insecure = UserRepositoryInsecure(db_name)

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(router_insecure, prefix="/insecure", tags=["Insecure Users"])

# Serve static HTML files
frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../Frontend"))

templates = Jinja2Templates(directory=frontend_dir)
img_dir = os.path.join(frontend_dir, "img")
style_dir = os.path.join(frontend_dir, "style")
script_file = os.path.join(frontend_dir, "script.js")

app.mount("/img", StaticFiles(directory=img_dir), name="img")
app.mount("/style", StaticFiles(directory=style_dir), name="style")

# Serve the single script.js file
@app.get("/script.js")
async def serve_script():
    with open(script_file, "r") as file:
        return file.read()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/booking", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("booking.html", {"request": request})
@app.get("/login", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
@app.get("/profile", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})
@app.get("/reservation", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("reservation.html", {"request": request})
@app.get("/register", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("sign-up.html", {"request": request})
@app.get("/forgotpassword", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("forgot-password.html", {"request": request})


# @app.on_event("startup")
# def startup_event():
#     print("Starting the application...")
#     repo_insecure.create_table_if_not_exists()
#     print("Tables checked or created successfully!")

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