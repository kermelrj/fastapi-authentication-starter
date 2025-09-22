from pydantic_settings import BaseSettings
from pydantic import AnyURL, Field

class Settings(BaseSettings):
    app_name: str = Field("FastAPI Clean Architecture", env="APP_NAME")
    admin_email: str = Field(default="dev")
    debug: bool = False

    #Security
    jwt_secret: str = "please-change-me"
    jwt_alg: str = "HS256"
    jwt_access_minutes: int = 60
    jwt_refresh_minutes: int = 60 * 24 * 7 # 7 days

    #Database
    db_url: AnyURL | str = "sqlite:///./app.db"

    #Cors
    cors_origins: list[str] = ["*"]

    #Observability
    log_level: str = "INFO"

    #File storage
    storage_driver: str = "local" # s3, gcs, azure, local
    storage_bucket: str | None  = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()