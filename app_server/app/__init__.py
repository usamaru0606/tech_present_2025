"""
FastAPIアプリケーションの初期化
"""

from fastapi import FastAPI
from app.api.endpoints import user
from app.db.sqlite import create_tables

app = FastAPI(title="Tech Present 2025")

# ルーターの登録
app.include_router(user.router, prefix="/api")

# アプリケーション起動時にデータベーステーブルを作成
@app.on_event("startup")
async def startup_event():
    create_tables()