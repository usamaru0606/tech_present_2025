"""
体重記録関連のスキーマ定義

このモジュールでは、体重記録に関するPydanticモデル
（リクエスト、レスポンスなど）を定義します。
"""

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class WeightRecordRequest(BaseModel):
    """体重記録のリクエストスキーマ"""
    id: str
    recordDate: str
    weight: float

class WeightRecordResponse(BaseModel):
    """体重記録のレスポンススキーマ"""
    success: bool

class WeightHistoryResponse(BaseModel):
    """体重履歴のレスポンススキーマ"""
    labels: Optional[List[str]] = None
    datasets: Optional[List[dict]] = None 