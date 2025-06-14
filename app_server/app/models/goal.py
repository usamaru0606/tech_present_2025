from sqlalchemy import Column, Integer, Float, String, Date, JSON
from app.db.base_class import Base

class GoalSetting(Base):
    """目標設定のデータベースモデル"""
    __tablename__ = "goal_settings"

    id = Column(Integer, primary_key=True, index=True)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    problem = Column(JSON, nullable=False)
    deadline = Column(Date, nullable=False)
    goal_weight = Column(Float, nullable=False) 