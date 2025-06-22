from dotenv import load_dotenv
import os

load_dotenv()  # .env を読み込み

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///health_data.db")