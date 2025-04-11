from utils.config_loader import DB_URL
import os

class AppConfig:
    SQLALCHEMY_DATABASE_URI = DB_URL
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")  # For security
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = AppConfig()
