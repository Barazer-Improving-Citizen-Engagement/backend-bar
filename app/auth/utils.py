from appwrite.client import Client
from appwrite.services.account import Account

def authenticate_user(client: Client, email: str, password: str):
    account_service = Account(client)
    try:
        session = account_service.create_session(email, password)
        return session
    except Exception as e:
        return None
