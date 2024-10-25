from sqlalchemy import Column, Integer, String
from app.core.database import Base, engine

class User(Base):
    """
    User class representing a user model.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        full_name (str): The full name of the user.
        hashed_password (str): The hashed password of the user.
        is_active (int): The active status of the user (1 for active, 0 for inactive).
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Integer, default=1)

Base.metadata.create_all(engine)
