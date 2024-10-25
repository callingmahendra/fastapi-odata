# fastapi-odata

## Project Description

This project is a FastAPI application that provides an OData API for managing user data. It includes features such as user creation, retrieval, updating, and deletion.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/callingmahendra/fastapi-odata.git
   cd fastapi-odata
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r src/requirements.txt
   ```

4. Run the application:
   ```bash
   uvicorn src.main:app --reload
   ```

## Usage Examples

### Create a User

To create a new user, send a POST request to the `/users/` endpoint with the following JSON payload:
```json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "full_name": "Test User",
  "password": "password123"
}
```

### Retrieve a User

To retrieve a user by ID, send a GET request to the `/users/{user_id}` endpoint.

### Update a User

To update a user, send a PUT request to the `/users/{user_id}` endpoint with the following JSON payload:
```json
{
  "username": "updateduser",
  "email": "updateduser@example.com",
  "full_name": "Updated User"
}
```

### Delete a User

To delete a user, send a DELETE request to the `/users/{user_id}` endpoint.
