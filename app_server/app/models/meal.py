"""
食事記録関連のデータベースモデル
"""

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.db.base_class import Base

class MealRecord(Base):
    """食事記録テーブル"""
    __tablename__ = "meal_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    record_date = Column(Date, nullable=False)
    meal_timing = Column(String, nullable=False)  # "朝食", "昼食", "夕食" など
    main_dish = Column(String, default="")  # 主食
    main_side = Column(String, default="")  # 主菜
    sub_side = Column(String, default="")  # 副菜
    soup = Column(String, default="")  # 汁物
    other = Column(String, default="")  # その他 