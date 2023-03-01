from fastapi import FastAPI, APIRouter, status

app = FastAPI()
router = APIRouter()


@router.get('/')
def get_books():
    """Get all books."""
    return "return a list of book items"


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_book():
    """Create a new book."""
    return "create book item"


@router.patch('/{book_id}')
def update_book(book_id: str):
    """Update a book."""
    return f"update book item with id {book_id}"


@router.get('/{book_id}')
def get_book(book_id: str):
    """Get a book."""
    return f"get book item with id {book_id}"


@router.delete('/{book_id}')
def delete_book(book_id: str):
    """Delete a book."""
    return f"delete book item with id {book_id}"


app.include_router(router, tags=['Books'], prefix='/api/books')


@app.get("/api/healthcheck")
def healthcheck():
    """Healthcheck endpoint to check if the service is up and running."""
    return {"message": "Service is up and running!"}
