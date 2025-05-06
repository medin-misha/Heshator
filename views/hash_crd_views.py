from fastapi import APIRouter
from typing import List
from schemas import CreateHash, ReturnHash
from controllers import create_hash, delete_hash, get_all_hashes

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
