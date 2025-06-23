"""
体重記録関連のAPIエンドポイント定義

このモジュールでは、体重記録に関するAPIエンドポイント
（体重の記録、取得など）を定義します。
"""

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.schemas.weight import WeightRecordRequest, WeightRecordResponse, WeightHistoryResponse
from app.crud.weight import create_weight_record, get_weight_history
from app.crud.goal import get_goal_setting_by_user_id
from app.db.deps import get_db
import logging
from datetime import datetime, timedelta

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 体重記録関連のルーターを作成
router = APIRouter()

def log_section(title: str):
    """セクションタイトルを装飾してログ出力"""
    border = '='*50
    logger.info(f"\n{border}")
    logger.info(f"== {title}")
    logger.info(f"== {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(border)

@router.post("/recordweight", response_model=WeightRecordResponse)
async def record_weight(request: Request, weight_data: WeightRecordRequest, db: Session = Depends(get_db)):
    """
    体重を記録するエンドポイント

    Args:
        request (Request): リクエストオブジェクト
        weight_data (WeightRecordRequest): 体重記録データ
            - id: ユーザーID
            - recordDate: 記録日
            - weight: 体重
        db (Session): データベースセッション（自動で注入）

    Returns:
        WeightRecordResponse: 記録成功時はsuccess=True

    Raises:
        HTTPException: データベースエラー時は500エラー
    """
    try:
        log_section("1. リクエスト受信")
        logger.info(f"[エンドポイント] /recordweight")
        logger.info(f"[メソッド] POST")
        
        log_section("2. リクエストヘッダーの確認")
        for key, value in request.headers.items():
            logger.info(f"{key}: {value}")

        log_section("3. リクエストボディの取得")
        body = await request.json()
        logger.info(f"Request body: {body}")
        
        log_section("4. データのバリデーション")
        logger.info("[パース済みデータ]")
        parsed_data = weight_data.model_dump_json(indent=2)
        logger.info(parsed_data)
        logger.info("\n[バリデーション結果] OK")

        log_section("5. データベース処理")
        logger.info("体重データをデータベースに保存中...")
        create_weight_record(
            db=db,
            user_id=weight_data.id,
            record_date=weight_data.recordDate,
            weight=weight_data.weight
        )
        logger.info("データベース処理完了")
        
        log_section("6. レスポンス送信")
        logger.info("ステータス: 成功")
        logger.info("レスポンスデータ: { success: true }")
        
        return WeightRecordResponse(success=True)

    except ValueError as e:
        log_section("日付フォーマットエラー")
        logger.error(f"日付フォーマットエラー: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail="Invalid date format. Use YYYY-MM-DD"
        )
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

@router.get("/recordweight/{user_id}", response_model=WeightHistoryResponse)
async def get_weight_records(request: Request, user_id: str, db: Session = Depends(get_db)):
    """
    ユーザーの体重記録履歴を取得するエンドポイント

    Args:
        request (Request): リクエストオブジェクト
        user_id (str): ユーザーID
        db (Session): データベースセッション（自動で注入）

    Returns:
        WeightHistoryResponse: グラフ用のデータ形式
            {
                "labels": ["日付1", "日付2", ...],
                "datasets": [{
                    "label": "体重 (kg)",
                    "data": [体重1, 体重2, ...]
                }]
            }

    Raises:
        HTTPException: データベースエラー時は500エラー
    """
    try:
        log_section("1. リクエスト受信")
        logger.info(f"[エンドポイント] /recordweight/{user_id}")
        logger.info(f"[メソッド] GET")
        
        log_section("2. リクエストヘッダーの確認")
        for key, value in request.headers.items():
            logger.info(f"{key}: {value}")

        log_section("3. データベース処理")
        logger.info("体重履歴をデータベースから取得中...")
        history = get_weight_history(db, user_id)
        logger.info("データベース処理完了")
        
        log_section("4. レスポンス送信")
        logger.info("ステータス: 成功")
        logger.info(f"レスポンスデータ: {history}")
        
        return history

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

@router.get("/weightcarditem/{user_id}")
async def get_weight_card_item(user_id: str, db: Session = Depends(get_db)):
    """
    ユーザーの体重カード情報を返すエンドポイント
    """
    # 最新の体重履歴を取得
    history = get_weight_history(db, user_id)
    weight = None
    lastMonthWeight = None
    if history and history["datasets"] and history["datasets"][0]["data"]:
        weight = history["datasets"][0]["data"][0]
        # 仮実装: 1ヶ月前の体重は今の体重-2kgとする
        lastMonthWeight = weight - 2 if weight is not None else None
    # 目標設定情報を取得
    goal = get_goal_setting_by_user_id(db, user_id)
    goalWeight = goal.goal_weight if goal else None
    goalDate = goal.deadline.strftime("%Y-%m-%d") if goal and goal.deadline else None
    startDate = goal.start_date.strftime("%Y-%m-%d") if goal and hasattr(goal, "start_date") and goal.start_date else None
    return {
        "weight": weight,
        "lastMonthWeight": lastMonthWeight,
        "goalWeight": goalWeight,
        "goalDate": goalDate,
        "startDate": startDate
    } 