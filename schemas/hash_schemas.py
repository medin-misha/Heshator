from pydantic import BaseModel

class BaseHash(BaseModel):
    string: str

class CreateHash(BaseHash):
    pass

class ReturnHash(BaseHash):
    hash: str