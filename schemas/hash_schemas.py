from pydantic import BaseModel, PositiveInt

class BaseHash(BaseModel):
    string: str

class CreateHash(BaseHash):
    timeout: PositiveInt

class ReturnHash(BaseHash):
    hash: str