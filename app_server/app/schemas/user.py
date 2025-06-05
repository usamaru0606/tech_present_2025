"""
ユーザー関連のPydanticスキーマ定義

このモジュールでは、ユーザーデータのバリデーションと
シリアライゼーション/デシリアライゼーションに使用する
Pydanticモデルを定義します。
"""

from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class UserCreate(BaseModel):
    """
    ユーザー作成時のリクエストボディスキーマ
    
    Attributes:
        firstName (str): 名
        lastName (str): 姓
        gender (str): 性別
        age (int): 年齢
        birthday (date): 生年月日
        mailAddress (EmailStr): メールアドレス
        password (str): パスワード
    """
    firstName: str
    lastName: str
    gender: str
    age: int
    birthday: date
    mailAddress: EmailStr
    password: str

    class Config:
        from_attributes = True  # V2での新しい設定名

class UserResponse(BaseModel):
    """
    ユーザー作成レスポンススキーマ
    """
    success: bool

class UserLogin(BaseModel):
    """
    ユーザーログイン時のリクエストボディスキーマ
    
    Attributes:
        email (EmailStr): メールアドレス
        password (str): パスワード
    """
    email: EmailStr
    password: str