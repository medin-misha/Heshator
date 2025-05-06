import hashlib


def hash_data(data: bytes) -> str:
    hash_object = hashlib.md5(data)
    return hash_object.hexdigest()

