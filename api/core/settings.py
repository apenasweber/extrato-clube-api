from pydantic import BaseSettings


class Settings(BaseSettings):
    USER: str
    PASSWORD: str
    class Config:
        env_file = ".env"


settings = Settings()
