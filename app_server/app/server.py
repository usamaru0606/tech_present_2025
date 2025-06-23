"""
FastAPIアプリケーションのサーバー設定モジュール

このモジュールでは、FastAPIアプリケーションの設定、ミドルウェアの追加、
ルーティングの設定などを行います。
"""

from fastapi import FastAPI
from app.api.endpoints import goal, meal, user, weight  # userモジュールをインポート
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging
from app.db import get_db_connection
from typing import List
from app.schemas.mealmenu import MealMenu

# ロギングの設定
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI(
    title="My FastAPI App",
    description="FastAPI と Nuxt.js を組み合わせたアプリケーション",
    version="1.0.0"
)

# CORSミドルウェアの設定
# フロントエンド（Nuxt.js）からのリクエストを許可
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:3000",  # Nuxt.jsの開発サーバーのIPアドレス
        "http://localhost:3000",   # Nuxt.jsの開発サーバーのlocalhostアドレス
    ],
    allow_credentials=True,
    allow_methods=["*"],  # 全HTTPメソッドを許可
    allow_headers=["*"],  # 全HTTPヘッダーを許可
)

# ユーザールーターの登録
app.include_router(goal.router)
app.include_router(meal.router)
app.include_router(user.router)
app.include_router(weight.router)

# ルートエンドポイント
@app.get("/")
def read_root():
    """
    ルートエンドポイント
    アプリケーションのウェルカムメッセージを返します。
    """
    return {"message": "Welcome to FastAPI with Nuxt.js"}

def start():
    """
    アプリケーションサーバーを起動する関数
    
    uvicornを使用してFastAPIアプリケーションを起動します。
    - host: 0.0.0.0 (全てのネットワークインターフェースでリッスン)
    - port: 8000
    - reload: 開発モードでホットリロードを有効化
    """
    uvicorn.run(
        "app.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
        access_log=True
    )

# ユーザーIDを指定して、そのユーザーの食事メニューを取得するエンドポイント
@app.get("/mealmenu/{user_id}", response_model=List[MealMenu])
def get_meal_menu(user_id: str):
    # SQLiteに接続する（db.py で定義された関数を使用）
    conn = get_db_connection()
    cursor = conn.cursor()

    # 指定したユーザーIDに対応する食事メニューを meal_menu テーブルから取得
    cursor.execute("""
        SELECT 
            date,          -- 日付
            timing,        -- 朝食・昼食・夕食などの食事タイミング
            staple_food,   -- 主食（ごはん、パンなど）
            main_dish,     -- 主菜（肉、魚など）
            side_dish,     -- 副菜（野菜料理など）
            soup,          -- 汁物（味噌汁など）
            others         -- その他（デザートや飲み物など）
        FROM meal_menu
        WHERE user_id = ?
    """, (user_id,))
    
    # 取得した全ての行を取得（list of sqlite3.Row）
    rows = cursor.fetchall()
    
    # 接続を閉じる
    conn.close()

    # データが存在しなければ、404エラーを返す
    if not rows:
        raise HTTPException(status_code=404, detail="Meal menu not found")

    # 取得した行を Pydantic モデル MealMenu のリストに変換して返す
    return [MealMenu(**dict(row)) for row in rows]
