from fastapi import FastAPI
#from app.api.api import api_router
from fastapi.middleware.cors import CORSMiddleware

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