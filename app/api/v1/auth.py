from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.db.models import User
from app.db.session import get_db
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.services.auth_service import create_user
from app.core.security import create_token, verify_password

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await db.execute(select(User).where(User.email == user.email))
    if existing_user.scalar():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = await create_user(user, db)
    token = create_token(new_user.email)

    return {
        "access_token": token,
        "user": {
            "id": new_user.id,
            "email": new_user.email
        }
    }

@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalar_one_or_none()

    if existing_user is None or not verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials")

    token = create_token(existing_user.email)

    return {
        "access_token": token,
        "user": {
            "id": existing_user.id,
            "email": existing_user.email
        }
    }
