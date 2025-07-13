from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from app.core.config import settings    
from app.db.models import User
from app.schemas.user import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import hash_password
from sqlalchemy.future import select
from app.core.config import settings
from jose import jwt

async def create_user(user: UserCreate, db: AsyncSession) -> User:
    db_user = User(email=user.email, hashed_password=hash_password(user.password))
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

def create_token(email: str) -> str:
    payload = {
        "sub": email,
        "exp": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60  # or use datetime
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token
