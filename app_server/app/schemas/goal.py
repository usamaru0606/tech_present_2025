from pydantic import BaseModel
from typing import Dict, Optional, List, Union
from datetime import date

class GoalSettingCreate(BaseModel):
    """目標設定の作成用スキーマ"""
    user_id: str
    id: Optional[int] = None
    height: float
    weight: float
    problem: Union[str, Dict[str, str]]
    goalDate: str
    goal_weight: float

class GoalSettingUpdate(BaseModel):
    """目標設定の更新用スキーマ"""
    problem: Optional[str] = None
    startDate: Optional[str] = None
    goalDate: Optional[str] = None
    goalWeight: Optional[float] = None

class GoalSettingResponse(BaseModel):
    """目標設定画面用のレスポンススキーマ"""
    weight: Optional[float] = None
    problems: List[str]

class GoalSettingUpdateResponse(BaseModel):
    success: bool 