"""
APIルーターの設定モジュール

このモジュールでは、アプリケーションのメインAPIルーターを設定し、
各エンドポイントのサブルーターを登録します。
"""

from fastapi import APIRouter
from app.api.endpoints import user, goal

# メインのAPIルーターを作成
api_router = APIRouter()

# ユーザー関連のエンドポイントを /users プレフィックスで登録
api_router.include_router(user.router, prefix="/users", tags=["users"])

# 目標設定関連のエンドポイントを登録
api_router.include_router(goal.router, tags=["goals"])