from sqlalchemy import Column, Integer, Float, String, Date, JSON, ForeignKey
from app.db.base_class import Base

class GoalSetting(Base):
    """目標設定のデータベースモデル"""
    __tablename__ = "goal_settings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.guid"), nullable=False, index=True)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    problem = Column(JSON, nullable=False)
    goal_date = Column(Date, nullable=False)
    goal_weight = Column(Float, nullable=False) 