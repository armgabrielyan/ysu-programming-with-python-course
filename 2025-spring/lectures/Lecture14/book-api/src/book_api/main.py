from fastapi import FastAPI

from .database.connection import create_db_and_tables
from .routers import books

create_db_and_tables()

app = FastAPI(
    title="Book API",
    description="An API for managing books",
    version="0.1.0",
)

app.include_router(books.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
