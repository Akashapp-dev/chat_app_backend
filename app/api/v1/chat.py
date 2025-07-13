from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.schemas.message import MessageCreate, MessageOut
from app.services import chat_service
from app.core.security import get_current_user

from app.db.models import User

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/send", response_model=MessageOut)
async def send_msg(
    message: MessageCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user_id = getattr(current_user, "id", None)
    if not isinstance(user_id, int):
        raise ValueError("Invalid user id")
    return await chat_service.send_message(
        db,
        sender_id=user_id,
        content=message.content
    )

@router.get("/messages", response_model=list[MessageOut])
async def get_messages(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await chat_service.list_messages(db)
