from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="OpenBanking API",
    description="Protected Banking API using Keycloak",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the OpenBanking API"
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }

app.include_router(router)