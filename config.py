from pydantic_settings import BaseSettings
import dotenv
from pathlib import Path, PosixPath
import os

BASE_DIR = Path(__file__).parent

dotenv.load_dotenv(dotenv_path=BASE_DIR / ".env")

class RedisSettings(BaseSettings):
    url: str = os.environ["redis_url"]


class Settings(BaseSettings):
    redis: RedisSettings = RedisSettings()
    base_dir: PosixPath = BASE_DIR


settings = Settings()
