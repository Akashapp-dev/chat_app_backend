from fastapi import FastAPI
from app.api.v1 import auth, chat
from app.core import security
from app.core.security import router as security_router

app = FastAPI()

app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(security.router)
@app.get("/")
def root():
    return {"message": "Backend is running"}
