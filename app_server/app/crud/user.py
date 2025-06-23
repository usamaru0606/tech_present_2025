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
    # height = float(user_dict.get("height", 0) or 0)
    # weight = float(user_dict.get("weight", 0) or 0)
    # problem = user_dict.get("problem", "")
    # goalDate = user_dict.get("goalDate", "")
    # goalWeight = float(user_dict.get("goalWeight", 0) or 0)

    # if all([height, weight, goalDate, goalWeight, problem]):
    #     goal_setting_data = {
    #         "user_id": guid,
    #         "height": height,
    #         "weight": weight,
    #         "problem": {"name": problem},
    #         "deadline": datetime.strptime(goalDate, '%Y/%m/%d').date() if goalDate else None,
    #         "goal_weight": goalWeight,
    #     }
    #     new_goal_setting = GoalSetting(**goal_setting_data)
    #     db.add(new_goal_setting)
    # Userモデルに存在しないフィールドを除去
    for k in ["height", "weight", "problem", "goalDate", "goalWeight"]:
        user_dict.pop(k, None)
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

def get_user_by_guid(db: Session, guid: str) -> Optional[User]:
    """
    GUIDでユーザー情報を取得する
    """
    return db.query(User).filter(User.guid == guid).first()

def delete_user(db: Session, user_id: str):
    """
    ユーザーID（guid）指定でユーザーを削除する
    """
    user = db.query(User).filter(User.guid == user_id).first()
    if user:
        db.delete(user)
        db.commit()