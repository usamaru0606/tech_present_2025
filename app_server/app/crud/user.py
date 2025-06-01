"""
ユーザー関連のCRUD操作を定義するモジュール

このモジュールでは、ユーザーデータに対するデータベース操作
（作成、読み取り、更新、削除）の関数を提供します。
"""

from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

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