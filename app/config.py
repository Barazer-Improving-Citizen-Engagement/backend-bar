import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Barazer Civic Platform"
    PROJECT_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    
    # Appwrite configuration
    APPWRITE_ENDPOINT: str = os.getenv("APPWRITE_ENDPOINT")
    APPWRITE_PROJECT_ID: str = os.getenv("APPWRITE_PROJECT_ID")
    APPWRITE_API_KEY: str = os.getenv("APPWRITE_API_KEY")
    
    # Google Cloud NLP configuration
    GOOGLE_APPLICATION_CREDENTIALS: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

settings = Settings()
