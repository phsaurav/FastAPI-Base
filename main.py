"""
Main entry point for this FastAPI Project
"""
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core import config, database

# Accounts module imports
from accounts import models as accounts_models
from accounts.api.v1 import accounts

# Blogs module imports
from blogs import models as blogs_models
from blogs.api.v1 import blogs

app = FastAPI()

# CORS
if not config.cfg.prod:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/")
def root():
    """
    Handle root route entry point to check server status
    """
    return "FastAPI Base Server Running Docker Updated with CICD"


accounts_models.Base.metadata.create_all(database.engine)
blogs_models.Base.metadata.create_all(database.engine)

app.include_router(blogs.router)
app.include_router(accounts.router)

if __name__ == "__main__":
    uvicorn.run(app, log_level=config.cfg.fastapi_log_level)
