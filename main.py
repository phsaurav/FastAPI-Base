"""
Main entry point for this FastAPI Project
"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    """
    Handle root route entry point to check server status
    """
    return "FastAPI Base Server Running"


# models.Base.metadata.create_all(engine)

# app.include_router(authentication.router)
# app.include_router(blog.router)
# app.include_router(user.router)
