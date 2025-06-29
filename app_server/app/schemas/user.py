"""
ユーザー関連のスキーマ定義

このモジュールでは、ユーザー管理に関するPydanticモデル
（リクエスト、レスポンスなど）を定義します。
"""

from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional, List

class UserCreate(BaseModel):
    """
    ユーザー作成時のリクエストボディスキーマ
    
    Attributes:
        firstName (str): 名
        lastName (str): 姓
        gender (str): 性別
        age (int): 年齢
        birthday (str): 生年月日（YYYY-MM-DD形式の文字列）
        mailAddress (EmailStr): メールアドレス
        password (str): パスワード
        height: Optional[float] = None
        weight: Optional[float] = None
        problem: Optional[str] = None
        goalDate: Optional[str] = None
        goalWeight: Optional[float] = None
    """
    firstName: str
    lastName: str
    gender: str
    age: int
    birthday: str
    mailAddress: EmailStr
    password: str
    height: Optional[float] = None
    weight: Optional[float] = None
    problem: Optional[str] = None
    goalDate: Optional[str] = None
    goalWeight: Optional[float] = None

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    """
    ユーザー作成レスポンススキーマ
    """
    success: bool
    guid: str

class UserLogin(BaseModel):
    """
    ユーザーログイン時のリクエストボディスキーマ
    
    Attributes:
        mailAddress (str): メールアドレス
        password (str): パスワード
    """
    mailAddress: str
    password: str

class UserLoginResponse(BaseModel):
    """ログイン成功時のレスポンススキーマ"""
    guid: str

class GoalSettingResponse(BaseModel):
    """目標設定画面用のレスポンススキーマ"""
    weight: Optional[float] = None
    problems: List[str]