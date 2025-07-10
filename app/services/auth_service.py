from app.core.security import hash_password, verify_password, create_token
from app.repositories import user_repo
from fastapi import HTTPException, status

async def register_user(db, user_data):
    existing_user = await user_repo.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user_data.password)
    new_user = await user_repo.create_user(db, user_data.email, hashed_pw)
    return new_user

async def login_user(db, user_data):
    user = await user_repo.get_user_by_email(db, user_data.email)
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": user.email})
    return token, user
