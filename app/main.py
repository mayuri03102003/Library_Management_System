from fastapi import FastAPI
from app.routers.book_router import router as book_router

app = FastAPI(title="Library Management System")

app.include_router(book_router)


@app.get("/")
def home():
    return {"message": "Library Management System API"}