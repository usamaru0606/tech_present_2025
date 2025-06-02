"""
ユーザー関連のAPIエンドポイント定義

このモジュールでは、ユーザー管理に関するAPIエンドポイント
（ユーザー登録、取得、更新、削除など）を定義します。
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.crud.user import create_user, authenticate_user
from app.db.deps import get_db
from typing import Dict

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

@router.post("/users/login/", response_model=Dict[str, str])
async def login_user(user_data: UserLogin, db: Session = Depends(get_db)):
    """
    ユーザーログインを処理するエンドポイント

    Args:
        user_data (UserLogin): ログイン情報（メールアドレス、パスワード）
        db (Session): データベースセッション（自動で注入）

    Returns:
        Dict[str, str]: 認証成功時はユーザーのGUIDを含む辞書

    Raises:
        HTTPException: 認証失敗時は401エラー
    """
    guid = authenticate_user(db, user_data)
    if not guid:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    return {"guid": guid}