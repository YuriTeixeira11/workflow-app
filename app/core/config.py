from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "backend-lab"
    DATABASE_URL: str = "sqlite:///./backend_lab.db"

    class Config:
        env_file = ".env"


settings = Settings()