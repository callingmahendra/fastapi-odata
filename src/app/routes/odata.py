from sqlalchemy import select
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from odata_query.sqlalchemy import apply_odata_query
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserSearch

router = APIRouter()

@router.post("/users")
def get_users(user_search: UserSearch, db: Session = Depends(get_db) ):
    try:

        orm_query = select(User)  # This is any form of Query or Selectable.
        users=[]
        if(user_search.filter):
            query = apply_odata_query(orm_query, user_search.filter)
            users = db.execute(query).scalars().all()
        print(users)
        return users
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
