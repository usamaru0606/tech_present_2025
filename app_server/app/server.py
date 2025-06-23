"""
FastAPIアプリケーションのサーバー設定モジュール

このモジュールでは、FastAPIアプリケーションの設定、ミドルウェアの追加、
ルーティングの設定などを行います。
"""

from . import app
import uvicorn

# このファイルは、uvicornの起動ターゲットとしてのみ使用します。
# アプリケーションのロジックや設定は、__init__.pyや他のモジュールで管理します。

def start():
    """
    アプリケーションサーバーを起動する関数
    
    uvicornを使用してFastAPIアプリケーションを起動します。
    """
    uvicorn.run(
        "app.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
        access_log=True
    )
