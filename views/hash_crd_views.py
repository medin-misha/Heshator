from fastapi import APIRouter
from schemas import CreateHash, ReturnHash
from controllers import create_hash

router = APIRouter(prefix="/hash", tags=["hash"])


@router.post("/")
async def create_hash_view(data: CreateHash) -> ReturnHash:
    return await create_hash(data=data)
