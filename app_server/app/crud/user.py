"""
ユーザー関連のCRUD操作を定義するモジュール

このモジュールでは、ユーザーデータに対するデータベース操作
（作成、読み取り、更新、削除）の関数を提供します。
"""

from sqlalchemy.orm import Session
from app.models.user import User
from app.models.goal import GoalSetting
from app.schemas.user import UserCreate, UserLogin
from typing import Optional
from datetime import datetime

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
    user_dict = user_data.model_dump()
    
    # 目標設定が全て埋まっている場合のみGoalSettingを作成
    if all([
        user_dict.get("height") is not None,
        user_dict.get("weight") is not None,
        user_dict.get("goalDate"),
        user_dict.get("goalWeight") is not None,
        user_dict.get("problem")
    ]):
        goal_setting_data = {
            "user_id": guid,
            "height": user_dict.pop("height"),
            "weight": user_dict.pop("weight"),
            "problem": {"name": user_dict.pop("problem")},
            "deadline": datetime.strptime(user_dict.pop("goalDate"), '%Y/%m/%d').date(),
            "goal_weight": user_dict.pop("goalWeight"),
        }
        new_goal_setting = GoalSetting(**goal_setting_data)
        db.add(new_goal_setting)
    else:
        user_dict.pop("height", None)
        user_dict.pop("weight", None)
        user_dict.pop("problem", None)
        user_dict.pop("goalDate", None)
        user_dict.pop("goalWeight", None)

    # startDateはUserCreateスキーマにはないので削除
    user_dict.pop("startDate", None)

    # メールアドレスのフィールド名を変更
    user_dict['email'] = user_dict.pop('mailAddress')
    
    # 文字列の日付をdate型に変換
    user_dict['birthday'] = datetime.strptime(user_dict.pop('birthday'), '%Y/%m/%d').date()
    
    # GUIDを追加
    user_dict['guid'] = guid
    
    # ユーザーモデルを作成
    new_user = User(**user_dict)
    
    # データベースに新規ユーザーと目標設定を追加
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
    # メールアドレスが空の場合は認証しない
    if not user_data.mailAddress:
        return None

    # メールアドレスでユーザーを検索
    user = db.query(User).filter(User.email == user_data.mailAddress).first()
    
    # ユーザーが存在し、パスワードが一致する場合はGUIDを返す
    if user and user.password == user_data.password:  # 注: 実際の実装ではパスワードハッシュを使用すべき
        return user.guid
    
    return None