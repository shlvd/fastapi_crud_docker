from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings for the app."""
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    class Config:
        """Config for the app."""
        env_file = './.env'


settings = Settings()

