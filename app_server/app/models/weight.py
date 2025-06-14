"""
体重記録のデータベースモデル定義
"""

from sqlalchemy import Column, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class WeightRecord(Base):
    """体重記録テーブル"""
    __tablename__ = "weight_records"

    id = Column(String(36), primary_key=True, index=True)  # ユーザーID
    record_date = Column(DateTime, nullable=False)  # 記録日
    weight = Column(Float, nullable=False)  # 体重

    def __repr__(self):
        return f"<WeightRecord(id={self.id}, date={self.record_date}, weight={self.weight})>" 