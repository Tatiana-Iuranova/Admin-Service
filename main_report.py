from fastapi import FastAPI
from routers.admin_report import report_router


app = FastAPI(docs_url=None, redoc_url=None)

app.include_router(report_router, prefix="/admin", tags=["Admin"])
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Admin Service API"}
