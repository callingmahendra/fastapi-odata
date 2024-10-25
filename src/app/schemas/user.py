from pydantic import BaseModel
from typing import Optional
from pydantic import ConfigDict

class User(BaseModel):
    """
    User model for representing user data.

    Attributes:
        id (int): The unique identifier for the user.
        username (str): The username of the user.
        email (str): The email address of the user.
        full_name (Optional[str]): The full name of the user.
        is_active (bool): The active status of the user.
    """
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    """
    UserCreate model for creating a new user.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        full_name (Optional[str]): The full name of the user.
        password (str): The password of the user.
    """
    username: str
    email: str
    full_name: Optional[str] = None
    password: str

class UserUpdate(BaseModel):
    """
    UserUpdate model for updating an existing user.

    Attributes:
        username (Optional[str]): The username of the user.
        email (Optional[str]): The email address of the user.
        full_name (Optional[str]): The full name of the user.
        password (Optional[str]): The password of the user.
        is_active (Optional[bool]): The active status of the user.
    """
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
