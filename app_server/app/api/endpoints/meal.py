"""
食事記録関連のAPIエンドポイント定義
"""

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.schemas.meal import MealRecordRequest, MealRecordResponse
from app.crud.meal import create_or_update_meal_record
from app.db.deps import get_db
import logging
import json
from datetime import datetime, timedelta
import openai
import os
from dotenv import load_dotenv
from app.service import gpt_mealmenu
from app.models.meal import MealRecord
from app.models.user import User
from app.models.goal import GoalSetting
from sqlalchemy import asc
import re

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 食事記録関連のルーターを作成
router = APIRouter()

def log_section(title: str):
    """セクションタイトルを装飾してログ出力"""
    border = '='*50
    logger.info(f"\n{border}")
    logger.info(f"== {title}")
    logger.info(f"== {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(border)

@router.post("/recordmeal", response_model=MealRecordResponse)
async def record_meal(
    request: Request,
    meal_record: MealRecordRequest,
    db: Session = Depends(get_db)
):
    """
    食事を記録するエンドポイント

    Args:
        request (Request): リクエストオブジェクト
        meal_record (MealRecordRequest): 食事記録データ
            - id: ユーザーID
            - recordDate: 記録日
            - mealTiming: 食事タイミング（朝食、昼食、夕食など）
            - content: 食事内容
        db (Session): データベースセッション（自動で注入）

    Returns:
        MealRecordResponse: 記録成功時はsuccess=True

    Raises:
        HTTPException: データベースエラー時は500エラー
    """
    try:
        log_section("1. リクエスト受信")
        logger.info(f"[エンドポイント] /recordmeal")
        logger.info(f"[メソッド] POST")
        
        log_section("2. リクエストヘッダーの確認")
        for key, value in request.headers.items():
            logger.info(f"{key}: {value}")

        log_section("3. リクエストボディの取得")
        body = await request.json()
        logger.info(json.dumps(body, ensure_ascii=False, indent=2))
        
        log_section("4. データのバリデーション")
        logger.info("[パース済みデータ]")
        parsed_data = meal_record.model_dump_json(indent=2)
        logger.info(parsed_data)
        logger.info("\n[バリデーション結果] OK")

        log_section("5. データベース処理")
        logger.info("食事記録データをデータベースに保存中...")
        create_or_update_meal_record(db, meal_record)
        logger.info("データベース処理完了")
        
        log_section("6. レスポンス送信")
        logger.info("ステータス: 成功")
        logger.info("レスポンスデータ: { success: true }")
        
        return MealRecordResponse(success=True)

    except Exception as e:
        log_section("エラー発生")
        logger.error(f"エラー発生箇所: {e.__traceback__.tb_frame.f_code.co_name}")
        logger.error(f"エラー種類: {type(e).__name__}")
        logger.error(f"エラー内容: {str(e)}")
        logger.error("エラー詳細:")
        import traceback
        logger.error(traceback.format_exc())
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.get("/todaymenu/{user_id}")
async def get_today_menu(user_id: str):
    """
    ユーザーの本日の食事メニュー（朝昼晩）を返すエンドポイント（仮実装）
    """
    return {
        "breakfast": {
            "stapleFood": "パン",
            "mainDish": "目玉焼き",
            "sideDish": "フルーツ",
            "soup": "スープ",
            "other": "コーヒー",
            "totalCalories": 450
        },
        "lunch": {
            "stapleFood": "パスタ",
            "mainDish": "ミートソース",
            "sideDish": "サラダ",
            "soup": "コンソメスープ",
            "other": "ヨーグルト",
            "totalCalories": 650
        },
        "dinner": {
            "stapleFood": "白ごはん",
            "mainDish": "焼き鮭",
            "sideDish": "お浸し",
            "soup": "味噌汁",
            "other": "なし",
            "totalCalories": 500
        }
    }

@router.post("/generate_weekly_meal/{user_id}")
async def generate_weekly_meal(user_id: str, db: Session = Depends(get_db)):
    """
    gpt_mealmenu.pyのロジックを使い、1週間分の食事メニューを生成しmeal_recordsに保存するAPI
    """
    # ユーザー情報取得
    user: User = db.query(User).filter(User.guid == user_id).first()
    goal: GoalSetting = db.query(GoalSetting).filter(GoalSetting.user_id == user_id).first()
    if not user or not goal:
        raise HTTPException(status_code=404, detail="ユーザー情報または目標設定が見つかりません")

    # gpt_mealmenu.pyのロジックを流用
    user_data = {
        "gender": user.gender,
        "age": user.age,
        "height": goal.height,
        "weight": goal.weight,
        "goal_weight": goal.goal_weight,
        "problem": goal.problem["name"] if isinstance(goal.problem, dict) and "name" in goal.problem else str(goal.problem)
    }
    timings = ["朝食", "昼食", "夕食"]
    week = []
    today = datetime.now().date()
    import json as pyjson
    menu_text = gpt_mealmenu.generate_meal_menu_text(user_data)
    # コードブロック記号を行単位で完全に除去
    lines = menu_text.splitlines()
    lines = [line for line in lines if not line.strip().startswith("```")]
    menu_text_clean = "\n".join(lines).strip()
    try:
        week_menus = pyjson.loads(menu_text_clean)
    except Exception as e:
        logger.error(f"GPT出力のパースに失敗: {str(e)}\n内容: {menu_text_clean}")
        raise HTTPException(status_code=500, detail=f"GPT出力のパースに失敗: {str(e)}")
    for i, day in enumerate(week_menus):
        record_date = today + timedelta(days=i)  # サーバー側で日付を割り当て
        day_meals = {}
        for timing in timings:
            meal = day.get(timing, {})
            logger.info(f"生成: {record_date} {timing} {meal}")
            calories = meal.get("カロリー", None)
            db_record = db.query(MealRecord).filter(
                MealRecord.user_id == user_id,
                MealRecord.record_date == record_date,
                MealRecord.meal_timing == timing
            ).first()
            if db_record:
                db_record.main_dish = meal.get("主食", "")
                db_record.main_side = meal.get("主菜", "")
                db_record.sub_side = meal.get("副菜", "")
                db_record.soup = meal.get("汁物", "")
                db_record.other = meal.get("その他", "")
                db_record.calories = calories
            else:
                db_record = MealRecord(
                    user_id=user_id,
                    record_date=record_date,
                    meal_timing=timing,
                    main_dish=meal.get("主食", ""),
                    main_side=meal.get("主菜", ""),
                    sub_side=meal.get("副菜", ""),
                    soup=meal.get("汁物", ""),
                    other=meal.get("その他", ""),
                    calories=calories
                )
                db.add(db_record)
            day_meals[timing] = {
                "stapleFood": meal.get("主食", ""),
                "mainDish": meal.get("主菜", ""),
                "sideDish": meal.get("副菜", ""),
                "soup": meal.get("汁物", ""),
                "other": meal.get("その他", ""),
                "calories": calories
            }
        week.append({
            "date": str(record_date),
            "breakfast": day_meals.get("朝食", {}),
            "lunch": day_meals.get("昼食", {}),
            "dinner": day_meals.get("夕食", {})
        })
    db.commit()
    return {"weekMeals": week}

@router.get("/weeklymeal/{user_id}")
async def get_weekly_meal(user_id: str, db: Session = Depends(get_db)):
    """
    meal_recordsテーブルから直近7日分の食事メニューを取得して返すAPI
    """
    from datetime import date, timedelta
    today = date.today()
    week_dates = [(today - timedelta(days=i)) for i in range(6, -1, -1)]
    records = db.query(MealRecord).filter(
        MealRecord.user_id == user_id,
        MealRecord.record_date.in_(week_dates)
    ).order_by(asc(MealRecord.record_date), asc(MealRecord.meal_timing)).all()

    # 日付ごとに朝昼晩をまとめる
    result = []
    for d in week_dates:
        day = {"date": str(d), "breakfast": {}, "lunch": {}, "dinner": {}}
        for rec in records:
            if rec.record_date == d:
                meal = {
                    "stapleFood": rec.main_dish or "",
                    "mainDish": rec.main_side or "",
                    "sideDish": rec.sub_side or "",
                    "soup": rec.soup or "",
                    "other": rec.other or ""
                }
                if rec.meal_timing == "朝食":
                    day["breakfast"] = meal
                elif rec.meal_timing == "昼食":
                    day["lunch"] = meal
                elif rec.meal_timing == "夕食":
                    day["dinner"] = meal
        result.append(day)
    return {"weekMeals": result} 