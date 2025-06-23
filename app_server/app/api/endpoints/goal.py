"""
目標設定関連のAPIエンドポイント定義

このモジュールでは、目標設定に関するAPIエンドポイント
（目標設定画面のデータ取得など）を定義します。
"""

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.schemas.goal import GoalSettingCreate, GoalSettingUpdate, GoalSettingResponse, GoalSettingUpdateResponse
from app.crud.goal import create_goal_setting, update_goal_setting
from app.db.deps import get_db
from app.schemas.user import GoalSettingResponse
import logging
import json
from datetime import datetime
from pydantic import ValidationError

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 目標設定関連のルーターを作成
router = APIRouter()

def log_section(title: str):
    """セクションタイトルを装飾してログ出力"""
    border = '='*50
    logger.info(f"\n{border}")
    logger.info(f"== {title}")
    logger.info(f"== {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(border)

@router.post("/goalsetting/create", response_model=GoalSettingResponse)
async def create_new_goal_setting(
    request: Request,
    goal_setting: GoalSettingCreate,
    db: Session = Depends(get_db)
):
    """
    新規目標設定を登録するエンドポイント
    user_id必須
    """
    try:
        log_section("1. リクエスト受信")
        logger.info(f"[エンドポイント] /goalsetting/create")
        logger.info(f"[メソッド] POST")
        log_section("2. リクエストヘッダーの確認")
        for key, value in request.headers.items():
            logger.info(f"{key}: {value}")
        log_section("3. リクエストボディの取得")
        body = await request.json()
        logger.info(json.dumps(body, ensure_ascii=False, indent=2))
        log_section("4. データのバリデーション")
        logger.info("[パース済みデータ]")
        parsed_data = goal_setting.model_dump_json(indent=2)
        logger.info(parsed_data)
        logger.info("\n[バリデーション結果] OK")
        log_section("5. データベース処理開始")
        logger.info("目標設定データをデータベースに挿入中...")
        create_goal_setting(db, goal_setting)
        logger.info("データベース処理完了")
        log_section("6. レスポンス送信")
        logger.info("ステータス: 成功")
        logger.info("レスポンスデータ: { success: true }")
        # 仮の値でレスポンスを返す（本来はDBから取得した値を返すべき）
        return GoalSettingResponse(
            weight=goal_setting.weight,
            problems=[goal_setting.problem["name"] if isinstance(goal_setting.problem, dict) and "name" in goal_setting.problem else str(goal_setting.problem)]
        )
    except ValidationError as e:
        log_section("バリデーションエラー")
        logger.error(f"バリデーションエラー: {str(e)}")
        raise HTTPException(
            status_code=422,
            detail=str(e)
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
            detail="Internal server error"
        )

@router.put("/goalsetting/{user_id}", response_model=GoalSettingUpdateResponse)
async def update_existing_goal_setting(
    user_id: str,
    goal_setting: GoalSettingUpdate,
    db: Session = Depends(get_db),
    request: Request = None,
):
    """
    既存の目標設定を更新するエンドポイント
    """
    try:
        log_section("1. リクエスト受信")
        logger.info(f"[エンドポイント] /goalsetting/update")
        logger.info(f"[メソッド] PUT")
        
        log_section("2. リクエストヘッダーの確認")
        for key, value in request.headers.items():
            logger.info(f"{key}: {value}")

        log_section("3. リクエストボディの取得")
        body = await request.json()
        logger.info(json.dumps(body, ensure_ascii=False, indent=2))
        
        log_section("4. データのバリデーション")
        logger.info("[パース済みデータ]")
        parsed_data = goal_setting.model_dump_json(indent=2)
        logger.info(parsed_data)
        logger.info("\n[バリデーション結果] OK")
        
        log_section("5. データベース処理開始")
        logger.info("目標設定データを更新中...")
        update_goal_setting(db, user_id=user_id, goal_setting_update=goal_setting)
        logger.info("データベース処理完了")
        
        log_section("6. レスポンス送信")
        logger.info("ステータス: 成功")
        logger.info("レスポンスデータ: { success: true }")
        
        return GoalSettingUpdateResponse(success=True)
        
    except ValidationError as e:
        log_section("バリデーションエラー")
        logger.error(f"バリデーションエラー: {str(e)}")
        raise HTTPException(
            status_code=422,
            detail=str(e)
        )
    except ValueError as e:
        log_section("データ不存在エラー")
        logger.error(f"データ不存在エラー: {str(e)}")
        raise HTTPException(
            status_code=404,
            detail=str(e)
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
            detail="Internal server error"
        )

@router.get("/goalsetting/{user_id}", response_model=GoalSettingResponse)
async def get_goal_setting(request: Request, user_id: str, db: Session = Depends(get_db)):
    """
    目標設定画面用のデータを取得するエンドポイント

    Args:
        request (Request): リクエストオブジェクト
        user_id (str): ユーザーID
        db (Session): データベースセッション（自動で注入）

    Returns:
        GoalSettingResponse: 体重と悩みのリストを含むレスポンス

    Raises:
        HTTPException: ユーザーが見つからない場合は404エラー
    """
    try:
        log_section("1. リクエスト受信")
        logger.info(f"[エンドポイント] /goalsetting/{user_id}")
        logger.info(f"[メソッド] GET")
        
        log_section("2. リクエストヘッダーの確認")
        for key, value in request.headers.items():
            logger.info(f"{key}: {value}")

        # TODO: データベースからユーザーの体重と悩みを取得する処理を実装
        # 仮のデータを返却
        return GoalSettingResponse(
            weight=None,  # 体重が取得できない場合はnull
            problems=["ダイエット", "運動不足", "食事管理"]  # 仮の悩みリスト
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