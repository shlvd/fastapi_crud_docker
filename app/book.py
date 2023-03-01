from . import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Response
from .database import get_db

router = APIRouter()


@router.get('/')
def get_books(db: Session = Depends(get_db),
              limit: int = 10,
              page: int = 1,
              search: str = ''
              ):
    """Get all books."""
    skip = (page - 1) * limit

    books = db.query(models.Book).filter(
        models.Book.title.contains(search)).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(books), 'Books': books}


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_book(payload: schemas.BookBaseSchema,
                db: Session = Depends(get_db)):
    """Create a new book."""
    new_book = models.Book(**payload.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"status": "success", "book": new_book}


@router.patch('/{book_id}')
def update_book(book_id: str,
                payload: schemas.BookBaseSchema,
                db: Session = Depends(get_db)
                ):
    """Update a book."""
    book_query = db.query(models.Book).filter(models.Book.id == book_id)
    db_book = book_query.first()

    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No Book with this id: {book_id} found')
    update_data = payload.dict(exclude_unset=True)
    book_query.filter(models.Book.id == book_id).update(
        update_data,
        synchronize_session=False)
    db.commit()
    db.refresh(db_book)
    return {"status": "success", "Book": db_book}


@router.get('/{book_id}')
def get_book(book_id: str, db: Session = Depends(get_db)):
    """Get a book."""
    book = db.query(models.book).filter(models.book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No book with this id: {id} found")
    return {"status": "success", "book": book}


@router.delete('/{book_id}')
def delete_book(book_id: str, db: Session = Depends(get_db)):
    """Delete a book."""
    book_query = db.query(models.Book).filter(models.book.id == book_id)
    book = book_query.first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No book with this id: {id} found")
    book_query.delete(synchronize_session=False)
    db.commit()
    return {"status": "success", "message": "Book deleted successfully"}
