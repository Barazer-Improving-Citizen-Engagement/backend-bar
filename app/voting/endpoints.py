from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from appwrite.client import Client
from appwrite.services.database import Database

voting_router = APIRouter()

client = Client()
client.set_endpoint('https://[HOSTNAME_OR_IP]/v1')
client.set_project('YOUR_PROJECT_ID')
client.set_key('YOUR_API_KEY')
database_service = Database(client)

class Vote(BaseModel):
    issue_id: str
    user_id: str
    vote: bool  # True for 'Yes', False for 'No'

@voting_router.post("/cast")
def cast_vote(vote: Vote):
    try:
        response = database_service.create_document(
            collection_id='VOTES_COLLECTION_ID',
            document_id='unique()',
            data={
                'issue_id': vote.issue_id,
                'user_id': vote.user_id,
                'vote': vote.vote
            }
        )
        return {"message": "Vote cast successfully", "vote_id": response['$id']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@voting_router.get("/results/{issue_id}")
def get_vote_results(issue_id: str):
    try:
        response = database_service.list_documents(collection_id='VOTES_COLLECTION_ID')
 
