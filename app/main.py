from fastapi import FastAPI
from app.api.v1 import auth, chat
from app.core import security
from app.core.security import router as security_router         
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import auth, chat
from app.core import security
from fastapi import FastAPI
from app.api.v1 import auth

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or use ["http://localhost:57362"] for tighter security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(security.router)
@app.get("/")
def root():
    return {"message": "Backend is running"}
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])