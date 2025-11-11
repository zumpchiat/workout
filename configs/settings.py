from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(default="mysql+aiomysql://root:root@localhost:3306/workout")


settings = Settings()
