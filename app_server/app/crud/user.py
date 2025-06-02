"""
ユーザー関連のCRUD操作を定義するモジュール

このモジュールでは、ユーザーデータに対するデータベース操作
（作成、読み取り、更新、削除）の関数を提供します。
"""

from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from typing import Optional

def create_user(db: Session, user_data: UserCreate) -> User:
    """
    新規ユーザーをデータベースに作成する

    Args:
        db (Session): データベースセッション
        user_data (UserCreate): 作成するユーザーのデータ

    Returns:
        User: 作成されたユーザーのモデルインスタンス
    """
    # パスワード確認フィールドを除外してユーザーモデルを作成
    new_user = User(**user_data.dict(exclude={"passwordConfirm"}))
    
    # データベースに新規ユーザーを追加
    db.add(new_user)
    db.commit()
    
    # 作成したユーザーを再取得して返す
    db.refresh(new_user)
    return new_user

def authenticate_user(db: Session, user_data: UserLogin) -> Optional[str]:
    """
    ユーザーの認証を行い、認証成功時にGUIDを返す

    Args:
        db (Session): データベースセッション
        user_data (UserLogin): ログイン情報（メールアドレス、パスワード）

    Returns:
        Optional[str]: 認証成功時はユーザーのGUID、失敗時はNone
    """
    # メールアドレスでユーザーを検索
    user = db.query(User).filter(User.email == user_data.email).first()
    
    # ユーザーが存在し、パスワードが一致する場合はGUIDを返す
    if user and user.password == user_data.password:  # 注: 実際の実装ではパスワードハッシュを使用すべき
        return user.guid
    
    return None