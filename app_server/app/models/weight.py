"""
体重記録のデータベースモデル定義
"""

from sqlalchemy import Column, String, Float, ForeignKey, DateTime, Integer
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime

class WeightRecord(Base):
    """体重記録テーブル"""
    __tablename__ = "weight_records"

    record_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(36), ForeignKey("users.guid"), nullable=False, index=True)
    record_date = Column(DateTime, nullable=False)
    weight = Column(Float, nullable=False)

    def __repr__(self):
        return f"<WeightRecord(id={self.record_id}, date={self.record_date}, weight={self.weight})>" 