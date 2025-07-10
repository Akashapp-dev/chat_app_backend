from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.db.session import get_db
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await auth_service.register_user(db, user)

@router.post("/login")
async def login(user: UserLogin, db: AsyncSession = Depends(get_db)):
    token, user_obj = await auth_service.login_user(db, user)
    return {"access_token": token, "user": user_obj}
