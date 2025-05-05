import hashlib
from encodings.utf_16_le import encode


def hash_data(data: bytes) -> str:
    hash_object = hashlib.sha256()
    hash_object.update(data)
    return hash_object.hexdigest()

