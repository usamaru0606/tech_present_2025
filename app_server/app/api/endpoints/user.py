"""
ユーザー関連のAPIエンドポイント定義

このモジュールでは、ユーザー管理に関するAPIエンドポイント
（ユーザー登録、取得、更新、削除など）を定義します。
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.crud.user import create_user
from app.db.deps import get_db

# ユーザー関連のルーターを作成
router = APIRouter()

@router.post("/users/")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    新規ユーザーを登録するエンドポイント

    Args:
        user (UserCreate): 登録するユーザーの情報
        db (Session): データベースセッション（自動で注入）

    Returns:
        User: 作成されたユーザーの情報
    """
    return create_user(db, user)