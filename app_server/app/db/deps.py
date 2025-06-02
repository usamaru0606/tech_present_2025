"""
データベース依存関係を定義するモジュール
"""

from typing import Generator
from sqlalchemy.orm import Session
from .sqlite import SessionLocal

def get_db() -> Generator[Session, None, None]:
    """
    FastAPIのDependencyとして使用するデータベースセッションを提供する
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 