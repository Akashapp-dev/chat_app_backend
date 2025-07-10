from app.repositories import message_repo

async def send_message(db, sender_id: int, content: str):
    return await message_repo.create_message(db, sender_id, content)

async def list_messages(db):
    return await message_repo.get_all_messages(db)
