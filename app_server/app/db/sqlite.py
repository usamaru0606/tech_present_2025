"""
SQLiteデータベース設定
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base_class import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLiteの場合に必要
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# データベーステーブルの作成
def create_tables():
    Base.metadata.create_all(bind=engine)