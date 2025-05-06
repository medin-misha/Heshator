from fastapi import HTTPException, status
from database import RedisDB
from controllers import hash_data
from schemas import CreateHash, ReturnHash
from config import settings


async def create_hash(data: CreateHash) -> ReturnHash:
    string = data.string

    hash = hash_data(data=string.encode())
    database = RedisDB(url=settings.redis.url)
    if await database.get(string):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This a string is in the database")
    else:
        await database.set(key=string, value=hash, timeout=data.timeout)
        return ReturnHash(string=string, hash=hash)


async def delete_hash(key: str) -> None:
    database = RedisDB(url=settings.redis.url)
    if await database.get(key):
        await database.delete(key=key)
        return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND
    )