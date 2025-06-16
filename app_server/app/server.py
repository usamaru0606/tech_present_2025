from fastapi import FastAPI, HTTPException
#from app.api.api import api_router
from fastapi.middleware.cors import CORSMiddleware

from typing import List
from db import get_db_connection
from schemas.mealmenu import MealMenu

app = FastAPI(
    title="My FastAPI App",
    description="FastAPI と Nuxt.js を組み合わせたアプリケーション",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API ルーターの登録
#app.include_router(api_router)

# ルートエンドポイント
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Nuxt.js"}

# エントリーポイントの関数
def start():
    import uvicorn
    uvicorn.run("app.server:app", host="0.0.0.0", port=8000, reload=True)

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