from pydantic import BaseModel
from typing import Dict, Optional, List
from datetime import date

class GoalSettingCreate(BaseModel):
    """目標設定の作成用スキーマ"""
    id: int
    height: float
    weight: float
    problem: Dict[str, str]
    deadline: date
    goal_weight: float

class GoalSettingUpdate(BaseModel):
    """目標設定の更新用スキーマ"""
    id: int
    problem: Dict[str, str]
    deadline: date
    goal_weight: float

class GoalSettingResponse(BaseModel):
    """目標設定画面用のレスポンススキーマ"""
    weight: Optional[float] = None
    problems: List[str] 