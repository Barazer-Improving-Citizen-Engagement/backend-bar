from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from appwrite.client import Client
from appwrite.services.database import Database

forum_router = APIRouter()

client = Client()
client.set_endpoint('https://[HOSTNAME_OR_IP]/v1')
client.set_project('YOUR_PROJECT_ID')
client.set_key('YOUR_API_KEY')
database_service = Database(client)

class ForumThread(BaseModel):
    title: str
    description: str
    created_by: str

@forum_router.post("/")
def create_thread(thread: ForumThread):
    try:
        response = database_service.create_document(
            collection_id='YOUR_COLLECTION_ID',
            document_id='unique()',
            data={
                'title': thread.title,
                'description': thread.description,
                'created_by': thread.created_by
            }
        )
        return {"message": "Thread created successfully", "thread_id": response['$id']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@forum_router.get("/")
def list_threads():
    try:
        response = database_service.list_documents(collection_id='YOUR_COLLECTION_ID')
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
