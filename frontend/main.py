from fastapi import FastAPI
app = FastAPI(title="任务管理 API", version="1.0.0")
@app.get("/")
async def root():
    return {"message": "欢迎使用任务管理 API"}
@app.get("/health")
async def health_check():
    return {"status": "ok"}