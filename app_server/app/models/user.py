"""
ユーザーテーブルのSQLAlchemyモデル定義

このモジュールでは、ユーザー情報を格納するデータベーステーブルの
モデルを定義します。SQLAlchemyのORMを使用してテーブルとPythonクラスを
マッピングします。
"""

from sqlalchemy import Column, Integer, String, Date
from app.db.sqlite import Base

class User(Base):
    """
    ユーザーテーブルのORMモデル
    
    Attributes:
        guid (str): ユーザーの一意識別子（主キー）
        name (str): ユーザー名
        gender (str): 性別
        age (int): 年齢
        birthday (date): 生年月日
        email (str): メールアドレス（一意制約あり）
        password (str): ハッシュ化されたパスワード
    """
    __tablename__ = "users"  # データベーステーブル名

    guid = Column(String, primary_key=True, index=True)  # 主キーかつインデックス
    name = Column(String, nullable=False)  # NULL不可
    gender = Column(String, nullable=False)  # NULL不可
    age = Column(Integer, nullable=False)  # NULL不可
    birthday = Column(Date, nullable=False)  # NULL不可
    email = Column(String, unique=True, nullable=False)  # 一意制約とNULL不可
    password = Column(String, nullable=False)  # NULL不可（ハッシュ化して保存）