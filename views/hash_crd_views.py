from fastapi import APIRouter
from schemas import CreateHash, ReturnHash
from controllers import create_hash
router = APIRouter(prefix="/hash", tags=["hash"])


@router.post("/")
async def create_hash_view(string: CreateHash) -> ReturnHash:
    return await create_hash(string=string)

