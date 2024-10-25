from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas import user as user_schema
from app.services import user as user_service

router = APIRouter()

def get_db():
    """
    Get a database session.

    This function provides a database session to be used within a context.
    It ensures that the session is properly closed after use.

    Yields:
        db (Session): A SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{user_id}", response_model=user_schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a user by ID.

    Args:
        user_id (int): The ID of the user to retrieve.
        db (Session): The database session.

    Returns:
        user_schema.User: The retrieved user.

    Raises:
        HTTPException: If the user is not found.
    """
    db_user = user_service.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.

    Args:
        user (user_schema.UserCreate): The user data for creating a new user.
        db (Session): The database session.

    Returns:
        user_schema.User: The created user.
    """
    return user_service.create_user(db, user)

@router.put("/{user_id}", response_model=user_schema.User)
def update_user(user_id: int, user: user_schema.UserUpdate, db: Session = Depends(get_db)):
    """
    Update an existing user.

    Args:
        user_id (int): The ID of the user to update.
        user (user_schema.UserUpdate): The updated user data.
        db (Session): The database session.

    Returns:
        user_schema.User: The updated user.

    Raises:
        HTTPException: If the user is not found.
    """
    db_user = user_service.update_user(db, user_id, user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=user_schema.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user by ID.

    Args:
        user_id (int): The ID of the user to delete.
        db (Session): The database session.

    Returns:
        user_schema.User: The deleted user.

    Raises:
        HTTPException: If the user is not found.
    """
    db_user = user_service.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
