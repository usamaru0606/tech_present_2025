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
from datetime import datetime

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