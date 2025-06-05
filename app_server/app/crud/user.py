"""
ユーザー関連のCRUD操作を定義するモジュール

このモジュールでは、ユーザーデータに対するデータベース操作
（作成、読み取り、更新、削除）の関数を提供します。
"""

from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from typing import Optional

def create_user(db: Session, user_data: UserCreate, guid: str) -> None:
    """
    新規ユーザーをデータベースに作成する

    Args:
        db (Session): データベースセッション
        user_data (UserCreate): 作成するユーザーのデータ
        guid (str): 生成されたGUID

    Returns:
        None
    """
    # ユーザーデータを辞書に変換
    user_dict = user_data.model_dump()
    
    # メールアドレスのフィールド名を変更
    user_dict['email'] = user_dict.pop('mailAddress')
    
    # 名前を結合
    user_dict['name'] = f"{user_dict.pop('lastName')} {user_dict.pop('firstName')}"
    
    # GUIDを追加
    user_dict['guid'] = guid
    
    # ユーザーモデルを作成
    new_user = User(**user_dict)
    
    # データベースに新規ユーザーを追加
    db.add(new_user)
    db.commit()

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