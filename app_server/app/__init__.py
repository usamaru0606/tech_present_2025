"""
FastAPIアプリケーションのメインパッケージ

このモジュールは、FastAPIアプリケーションのエントリーポイントとなるappオブジェクトと
サーバーを起動するstart関数をエクスポートします。
"""

from .server import app, start

__all__ = ["app", "start"]