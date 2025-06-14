from pydantic import BaseModel
from typing import Dict
from datetime import date

class GoalSettingCreate(BaseModel):
    """目標設定の作成用スキーマ"""
    id: int
    height: float
    weight: float
    problem: Dict[str, str]
    deadline: date
    goal_weight: float

class GoalSettingResponse(BaseModel):
    """目標設定のレスポンス用スキーマ"""
    success: bool 