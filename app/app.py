from app import models, book
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(book.router, tags=['Books'], prefix='/api/books')


@app.get("/api/healthcheck")
def root():
    """Health check endpoint."""
    return {"message": "The app is up and running."}
