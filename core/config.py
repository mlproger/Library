from pathlib import Path
from pydantic_settings import BaseSettings

Base_dir = Path(__file__).parent.parent
print(Base_dir)


class Config(BaseSettings):
    api_v1_prefix:str = "/api/v1"
    db_url: str = f"sqlite+aiosqlite:///{Base_dir}/db.sqlite3"
    db_echo: bool = True


config = Config()
