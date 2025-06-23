"""
食事記録関連のCRUD操作
"""

from sqlalchemy.orm import Session
from app.models.meal import MealRecord
from app.schemas.meal import MealRecordRequest
from datetime import datetime

def create_or_update_meal_record(db: Session, meal_record: MealRecordRequest) -> MealRecord:
    """
    食事記録を作成または更新する

    Args:
        db (Session): データベースセッション
        meal_record (MealRecordRequest): 食事記録データ

    Returns:
        MealRecord: 作成または更新された食事記録
    """
    # recordDateをdate型に変換
    if isinstance(meal_record.recordDate, str):
        try:
            if "/" in meal_record.recordDate:
                record_date_obj = datetime.strptime(meal_record.recordDate, "%Y/%m/%d").date()
            else:
                record_date_obj = datetime.strptime(meal_record.recordDate, "%Y-%m-%d").date()
        except Exception:
            raise ValueError("recordDateの形式が不正です")
    else:
        record_date_obj = meal_record.recordDate

    # 既存の記録を検索
    existing_record = db.query(MealRecord).filter(
        MealRecord.user_id == meal_record.id,
        MealRecord.record_date == record_date_obj,
        MealRecord.meal_timing == meal_record.mealTiming
    ).first()

    if existing_record:
        # 既存の記録を更新
        existing_record.main_dish = meal_record.content.主食
        existing_record.main_side = meal_record.content.主菜
        existing_record.sub_side = meal_record.content.副菜
        existing_record.soup = meal_record.content.汁物
        existing_record.other = meal_record.content.その他
        # カロリーも更新（あれば）
        if hasattr(meal_record.content, 'カロリー'):
            existing_record.calories = getattr(meal_record.content, 'カロリー', None)
        db.commit()
        db.refresh(existing_record)
        return existing_record
    else:
        # 新規記録を作成
        db_meal_record = MealRecord(
            user_id=meal_record.id,
            record_date=record_date_obj,
            meal_timing=meal_record.mealTiming,
            main_dish=meal_record.content.主食,
            main_side=meal_record.content.主菜,
            sub_side=meal_record.content.副菜,
            soup=meal_record.content.汁物,
            other=meal_record.content.その他,
            calories=getattr(meal_record.content, 'カロリー', None)
        )
        db.add(db_meal_record)
        db.commit()
        db.refresh(db_meal_record)
        return db_meal_record 