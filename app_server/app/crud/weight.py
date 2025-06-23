"""
体重記録のCRUD操作
"""

from sqlalchemy.orm import Session
from app.models.weight import WeightRecord
from datetime import datetime
from typing import Optional, List, Dict
from sqlalchemy import desc

def create_weight_record(db: Session, user_id: str, record_date: str, weight: float) -> WeightRecord:
    """
    体重記録を作成する

    Args:
        db (Session): データベースセッション
        user_id (str): ユーザーID
        record_date (str): 記録日（YYYY-MM-DD形式）
        weight (float): 体重

    Returns:
        WeightRecord: 作成された体重記録
    """
    # 文字列の日付をdatetime型に変換
    date_obj = datetime.strptime(record_date, "%Y/%m/%d")
    
    # 体重記録を作成
    db_weight = WeightRecord(
        user_id=user_id,
        record_date=date_obj,
        weight=weight
    )
    
    # データベースに保存
    db.add(db_weight)
    db.commit()
    db.refresh(db_weight)
    
    return db_weight

def get_weight_records(db: Session, user_id: str) -> list[WeightRecord]:
    """
    ユーザーの体重記録を取得する

    Args:
        db (Session): データベースセッション
        user_id (str): ユーザーID

    Returns:
        list[WeightRecord]: 体重記録のリスト
    """
    return db.query(WeightRecord).filter(WeightRecord.user_id == user_id).all()

def get_weight_history(db: Session, user_id: str) -> Dict:
    """
    ユーザーの体重履歴を取得する

    Args:
        db (Session): データベースセッション
        user_id (str): ユーザーID

    Returns:
        Dict: グラフ用のデータ形式
            {
                "labels": ["日付1", "日付2", ...],
                "datasets": [{
                    "label": "体重 (kg)",
                    "data": [体重1, 体重2, ...]
                }]
            }
    """
    # 体重記録を日付の降順で取得
    records = db.query(WeightRecord)\
        .filter(WeightRecord.user_id == user_id)\
        .order_by(desc(WeightRecord.record_date))\
        .all()
    
    if not records:
        return {"labels": None, "datasets": None}
    
    # 日付と体重のリストを作成
    labels = [record.record_date.strftime("%m/%d") for record in records]
    weights = [record.weight for record in records]
    
    return {
        "labels": labels,
        "datasets": [{
            "label": "体重 (kg)",
            "data": weights
        }]
    } 