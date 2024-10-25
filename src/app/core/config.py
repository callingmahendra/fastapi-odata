class Settings:
    """
    Settings class to store configuration variables.

    Attributes:
        DATABASE_URL (str): The URL for the database connection.
        SECRET_KEY (str): The secret key for the application.
    """
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "supersecretkey"

settings = Settings()
