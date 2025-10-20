"""
Application configuration module.
Handles environment variables and application settings.
"""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Application
    app_name: str = "Task Tracker API"
    app_version: str = "1.0.0"
    debug: bool = True
    environment: str = "development"
    
    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Database
    database_url: str = "postgresql://user:password@localhost:5432/task_tracker_db"
    postgres_user: str = "user"
    postgres_password: str = "password"
    postgres_db: str = "task_tracker_db"
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    
    # JWT
    secret_key: str = "your-secret-key-here-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7
    
    # CORS
    allowed_origins: List[str] = ["http://localhost:3000", "http://localhost:8000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Create settings instance
settings = Settings()
