"""
FastAPIアプリケーションの初期化
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import user, goal, meal, weight
from app.db.sqlite import create_tables
from app.models.user import User
from app.models.goal import GoalSetting
from app.models.weight import WeightRecord
from app.models.meal import MealRecord
from app.models.training import RecordTraining

app = FastAPI(title="Tech Present 2025")

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可
    allow_headers=["*"],  # すべてのヘッダーを許可
)

# ルーターの登録
app.include_router(user.router, prefix="/api")
app.include_router(goal.router, prefix="/api")
app.include_router(meal.router, prefix="/api")
app.include_router(weight.router, prefix="/api")

# アプリケーション起動時にデータベーステーブルを作成
@app.on_event("startup")
async def startup_event():
    create_tables()