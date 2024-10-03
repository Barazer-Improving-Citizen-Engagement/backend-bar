from fastapi import FastAPI
from app.auth.endpoints import auth_router
from app.forums.endpoints import forum_router
from app.voting.endpoints import voting_router
from app.ussd.endpoints import ussd_router
from app.nlp.endpoints import nlp_router

app = FastAPI(
    title="Barazer Civic Platform API",
    description="Backend services for civic engagement and governance platform",
    version="1.0.0"
)

# Include routers for each module
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(forum_router, prefix="/forums", tags=["Forums"])
app.include_router(voting_router, prefix="/voting", tags=["Voting"])
app.include_router(ussd_router, prefix="/ussd", tags=["USSD"])
app.include_router(nlp_router, prefix="/nlp", tags=["NLP & Sentiment Analysis"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Barazer Civic Platform API"}
