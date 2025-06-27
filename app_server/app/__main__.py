"""
アプリケーションのエントリーポイント

このモジュールは、pythonコマンドで直接実行された場合に
アプリケーションサーバーを起動します。
"""

if __name__ == '__main__':
    from .server import start
    start()  # サーバーを起動