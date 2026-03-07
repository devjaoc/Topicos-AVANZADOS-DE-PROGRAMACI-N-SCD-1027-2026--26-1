
import os
from dotenv import load_dotenv
from dataclasses import dataclass

load_dotenv()

@dataclass
class AppConfig:
    APP_ENV: str
    DB_URL: str

    @staticmethod
    def load():
        config = AppConfig(
            APP_ENV=os.getenv("APP_ENV", "development"),
            DB_URL=os.getenv("DB_URL"),
        )

        if not config.DB_URL:
            raise ValueError("DB_URL no está definido en .env")

        return config
