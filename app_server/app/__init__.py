"""
FastAPIアプリケーションの初期化
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import user
from app.db.sqlite import create_tables

app = FastAPI(title="Tech Present 2025")

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Nuxt.jsのデフォルトポート
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可
    allow_headers=["*"],  # すべてのヘッダーを許可
)

# ルーターの登録
app.include_router(user.router, prefix="/api")

# アプリケーション起動時にデータベーステーブルを作成
@app.on_event("startup")
async def startup_event():
    create_tables()