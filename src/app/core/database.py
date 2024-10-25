from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
"""
SQLAlchemy engine for database connection.

This engine is used to connect to the database specified by the DATABASE_URL.
"""

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
SQLAlchemy session factory.

This session factory is used to create database sessions for interacting with the database.
"""

Base = declarative_base()


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
