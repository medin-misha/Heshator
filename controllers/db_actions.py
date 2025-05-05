from database import RedisDB
from controllers import hash_data
from schemas import CreateHash, ReturnHash
from config import settings

async def create_hash(string: CreateHash) -> ReturnHash:
    string = string.string
    hash = hash_data(data=string.encode())
    database = RedisDB(url=settings.redis.url)
    await database.set(key=string, value=hash)
    return ReturnHash(string=string, hash=hash)

