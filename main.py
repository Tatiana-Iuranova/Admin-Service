from fastapi import FastAPI
from routers import admin_users

app = FastAPI()
app.include_router(admin_users.router)
