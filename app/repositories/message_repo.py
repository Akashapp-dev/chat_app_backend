from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Message

async def create_message(db: AsyncSession, sender_id: int, content: str):
    message = Message(sender_id=sender_id, content=content)
    db.add(message)
    await db.commit()
    await db.refresh(message)
    return message

async def get_all_messages(db: AsyncSession):
    result = await db.execute(select(Message).order_by(Message.timestamp))
    return result.scalars().all()
