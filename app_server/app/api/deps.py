"""
API依存関係（Dependency Injection）の定義モジュール

このモジュールでは、FastAPIエンドポイントで使用される
依存関係（データベースセッションなど）を定義します。
"""

from typing import Generator
from sqlalchemy.orm import Session
from app.db.sqlite import SessionLocal

def get_db() -> Generator[Session, None, None]:
    """
    リクエストごとのデータベースセッションを提供する依存関係

    FastAPIのDependency Injectionシステムで使用され、
    各リクエストに新しいデータベースセッションを提供します。
    セッションは自動的にクローズされます。

    Yields:
        Session: SQLAlchemyデータベースセッション
    """
    db = SessionLocal()  # 新しいセッションを作成
    try:
        yield db  # セッションをエンドポイントに提供
    finally:
        db.close()  # リクエスト完了後にセッションを確実にクローズ