from fastapi import FastAPI
from app.routes.user import router as user_router
from app.routes.odata import router as odata_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(odata_router, prefix="/odata", tags=["odata"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}
