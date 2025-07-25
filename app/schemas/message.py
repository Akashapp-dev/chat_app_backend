from pydantic import BaseModel
from datetime import datetime

class MessageCreate(BaseModel):
    content: str

class MessageOut(BaseModel):
    id: int
    sender_id: int
    content: str
    timestamp: datetime

    class Config:
        orm_mode = True
