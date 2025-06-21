"""
食事記録関連のスキーマ定義
"""

from pydantic import BaseModel
from typing import Optional
from datetime import date

class MealContent(BaseModel):
    """食事内容のスキーマ"""
    主食: str = ""
    主菜: str = ""
    副菜: str = ""
    汁物: str = ""
    その他: str = ""

class MealRecordRequest(BaseModel):
    """食事記録リクエストのスキーマ"""
    id: int
    recordDate: date
    mealTiming: str  # "朝食", "昼食", "夕食" など
    content: MealContent

class MealRecordResponse(BaseModel):
    """食事記録レスポンスのスキーマ"""
    success: bool 