"""
FastAPIアプリケーションのサーバー設定モジュール

このモジュールでは、FastAPIアプリケーションの設定、ミドルウェアの追加、
ルーティングの設定などを行います。
"""

from fastapi import FastAPI
from app.api.endpoints import user  # userモジュールをインポート
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging

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
app.include_router(user.router)

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