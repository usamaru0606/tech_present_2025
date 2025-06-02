"""
ユーザーモデルの定義
"""

from sqlalchemy import Column, String, Integer, Date
from app.db.base_class import Base

class User(Base):
    """
    ユーザーテーブルのモデル定義
    """
    __tablename__ = "users"

    guid = Column(String, primary_key=True, index=True)
    name = Column(String)
    gender = Column(String)
    age = Column(Integer)
    birthday = Column(Date)
    email = Column(String, unique=True, index=True)
    password = Column(String)  # 実際の実装ではハッシュ化したパスワードを保存