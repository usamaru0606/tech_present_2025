"""
SQLiteデータベース設定
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base_class import Base
import os
import sqlite3

# データベースファイルのパスを設定
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(DB_DIR, "app.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLiteの場合に必要
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# データベーステーブルの作成
def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), "app.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn