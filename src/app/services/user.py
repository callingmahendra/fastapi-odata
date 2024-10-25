from sqlalchemy.orm import Session
from app.models import user as user_model
from app.schemas import user as user_schema

def get_user(db: Session, user_id: int):
    """
    Retrieve a user by ID.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to retrieve.

    Returns:
        user_model.User: The retrieved user or None if not found.
    """
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()

def create_user(db: Session, user: user_schema.UserCreate):
    """
    Create a new user.

    Args:
        db (Session): The database session.
        user (user_schema.UserCreate): The user data for creating a new user.

    Returns:
        user_model.User: The created user.
    """
    db_user = user_model.User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=user.password,
        is_active=True
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: user_schema.UserUpdate):
    """
    Update an existing user.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to update.
        user (user_schema.UserUpdate): The updated user data.

    Returns:
        user_model.User: The updated user or None if not found.
    """
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if db_user:
        if user.username is not None:
            db_user.username = user.username
        if user.email is not None:
            db_user.email = user.email
        if user.full_name is not None:
            db_user.full_name = user.full_name
        if user.password is not None:
            db_user.hashed_password = user.password
        if user.is_active is not None:
            db_user.is_active = user.is_active
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    """
    Delete a user by ID.

    Args:
        db (Session): The database session.
        user_id (int): The ID of the user to delete.

    Returns:
        user_model.User: The deleted user or None if not found.
    """
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
