from fastapi import APIRouter
from typing import List
from schemas import CreateHash, ReturnHash
from controllers import create_hash, delete_hash, get_all_hashes, get_hash_by_key

router = APIRouter(prefix="/hash", tags=["hash"])


@router.post("/")
async def create_hash_view(data: CreateHash) -> ReturnHash:
    return await create_hash(data=data)


@router.delete("/{key}", status_code=204)
async def delete_hash_view(key: str) -> None:
    return await delete_hash(key=key)


@router.get("/")
async def get_all_hashes_view() -> List[str]:
    return await get_all_hashes()

@router.get("/{key}")
async def get_hash_by_key_view(key: str) -> str:
    return await get_hash_by_key(key=key)