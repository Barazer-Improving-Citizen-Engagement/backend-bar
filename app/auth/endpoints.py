from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.auth.utils import create_user, authenticate_user
from appwrite.client import Client
from appwrite.services.users import Users

auth_router = APIRouter()

# Initialize Appwrite client
client = Client()
client.set_endpoint('https://[HOSTNAME_OR_IP]/v1')  # Your Appwrite endpoint
client.set_project('YOUR_PROJECT_ID')  # Your Appwrite project ID
client.set_key('YOUR_API_KEY')  # Your Appwrite API key

class User(BaseModel):
    email: str
    password: str

@auth_router.post("/register")
def register_user(user: User):
    try:
        user_service = Users(client)
        user_response = user_service.create(
            user_id='unique()', 
            email=user.email,
            password=user.password
        )
        return {"message": "User registered successfully", "user_id": user_response['$id']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@auth_router.post("/login")
def login_user(user: User):
    authenticated_user = authenticate_user(client, user.email, user.password)
    if not authenticated_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": authenticated_user['$id']}
