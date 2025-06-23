"""
ユーザー関連のAPIエンドポイント定義

このモジュールでは、ユーザー管理に関するAPIエンドポイント
（ユーザー登録、取得、更新、削除など）を定義します。
"""

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin, UserResponse, UserLoginResponse
from app.crud.user import create_user, authenticate_user, delete_user
from app.db.deps import get_db
import uuid
import logging
import json
from datetime import datetime
from pydantic import ValidationError

# ロガーの設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ユーザー関連のルーターを作成
router = APIRouter()

def log_section(title: str):
    """セクションタイトルを装飾してログ出力"""
    border = '='*50
    logger.info(f"\n{border}")
    logger.info(f"== {title}")
    logger.info(f"== {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(border)

@router.post("/user/add", response_model=UserResponse)
async def register_user(request: Request, user: UserCreate, db: Session = Depends(get_db)):
    """
    新規ユーザーを登録するエンドポイント

    Args:
        request (Request): リクエストオブジェクト
        user (UserCreate): 登録するユーザーの情報
        db (Session): データベースセッション（自動で注入）

    Returns:
        UserResponse: 登録成功時はsuccess=True
    """
    try:
        log_section("1. リクエスト受信")
        logger.info(f"[エンドポイント] /user/add")
        logger.info(f"[メソッド] POST")
        
        log_section("2. リクエストヘッダーの確認")
        for key, value in request.headers.items():
            logger.info(f"{key}: {value}")

        log_section("3. リクエストボディの取得")
        body = await request.json()
        logger.info(json.dumps(body, ensure_ascii=False, indent=2))
        
        log_section("4. データのバリデーション")
        logger.info("[パース済みデータ]")
        parsed_data = user.model_dump_json(indent=2)
        logger.info(parsed_data)
        logger.info("\n[バリデーション結果] OK")

        log_section("5. GUID生成")
        user_guid = str(uuid.uuid4())
        logger.info(f"生成されたGUID: {user_guid}")
        
        log_section("6. データベース処理開始")
        logger.info("ユーザーデータをデータベースに挿入中...")
        create_user(db, user, user_guid)
        logger.info("データベース処理完了")
        
        log_section("7. レスポンス送信")
        logger.info("ステータス: 成功")
        logger.info("レスポンスデータ: { success: true }")
        
        return UserResponse(success=True, guid=user_guid)
        
    except Exception as e:
        log_section("エラー発生")
        logger.error(f"エラー発生箇所: {e.__traceback__.tb_frame.f_code.co_name}")
        logger.error(f"エラー種類: {type(e).__name__}")
        logger.error(f"エラー内容: {str(e)}")
        logger.error("エラー詳細:")
        import traceback
        logger.error(traceback.format_exc())
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@router.post("/user/login", response_model=UserLoginResponse)
async def login_user(request: Request, user_data: UserLogin, db: Session = Depends(get_db)):
    """
    ユーザーログインを処理するエンドポイント

    Args:
        request (Request): リクエストオブジェクト
        user_data (UserLogin): ログイン情報（メールアドレス、パスワード）
        db (Session): データベースセッション（自動で注入）

    Returns:
        UserLoginResponse: 認証成功時はユーザーのGUIDを含むレスポンス

    Raises:
        HTTPException: 認証失敗時は401エラー
    """
    try:
        log_section("1. リクエスト受信")
        logger.info(f"[エンドポイント] /user/login")
        logger.info(f"[メソッド] POST")
        
        log_section("2. リクエストヘッダーの確認")
        for key, value in request.headers.items():
            logger.info(f"{key}: {value}")

        log_section("3. リクエストボディの取得")
        body = await request.body()
        logger.info(f"Raw request body: {body.decode()}")
        
        log_section("4. パース済みデータの確認")
        logger.info(f"Parsed user_data: {user_data.model_dump_json()}")

        guid = authenticate_user(db, user_data)
        if not guid:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )
        return UserLoginResponse(guid=guid)
    except ValidationError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(
            status_code=422,
            detail=str(e)
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )

@router.delete("/user/delete/{user_id}")
async def delete_user_endpoint(user_id: str, db: Session = Depends(get_db)):
    """
    ユーザーID（guid）指定でユーザーを削除するエンドポイント
    """
    try:
        delete_user(db, user_id)
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))