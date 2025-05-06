import redis.asyncio as redis
from redis.typing import ResponseT, EncodableT, KeyT


class RedisDatabase():
    def __init__(self, url: str):
        self.redis_connect: redis.client.Redis = redis.from_url(url)

    async def set(self, key: KeyT, value: EncodableT, timeout: int = None) -> None:
        async with self.redis_connect.pipeline(transaction=True) as pipe:
            stmt = await pipe.set(name=key, value=value, ex=timeout)
            response = await stmt.execute()
            return response[0]

    async def get(self, key: KeyT) -> ResponseT:
        async with self.redis_connect.pipeline(transaction=True) as pipe:
            stmt = await pipe.get(key)
            response = await stmt.execute()
            return response[0]

    async def delete(self, key: KeyT) -> None:
        async with self.redis_connect.pipeline(transaction=True) as pipe:
            stmt = await pipe.getdel(name=key)
            await stmt.execute()
