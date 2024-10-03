from appwrite.client import Client
from appwrite.services.database import Database
from app.config import settings

def get_database_client() -> Database:
    client = Client()
    client.set_endpoint(settings.APPWRITE_ENDPOINT)
    client.set_project(settings.APPWRITE_PROJECT_ID)
    client.set_key(settings.APPWRITE_API_KEY)
    return Database(client)
