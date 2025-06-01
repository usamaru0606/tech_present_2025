"""
ユーザー関連のPydanticスキーマ定義

このモジュールでは、ユーザーデータのバリデーションと
シリアライゼーション/デシリアライゼーションに使用する
Pydanticモデルを定義します。
"""

from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    """
    ユーザー作成時のリクエストボディスキーマ
    
    Attributes:
        guid (str): ユーザーの一意識別子
        name (str): ユーザー名
        gender (str): 性別
        age (int): 年齢
        birthday (date): 生年月日
        email (EmailStr): メールアドレス
        password (str): パスワード
        passwordConfirm (str): パスワード確認用
    """
    guid: str
    name: str
    gender: str
    age: int
    birthday: date
    email: EmailStr
    password: str
    passwordConfirm: str

    class Config:
        orm_mode = True  # ORMモデルとの互換性を有効化