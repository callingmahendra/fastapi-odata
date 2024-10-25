from sqlalchemy import select
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from odata_query.sqlalchemy import apply_odata_query
from app.core.database import get_db
from app.models.user import User

router = APIRouter()

@router.post("/users")
def get_users(db: Session = Depends(get_db), filter: str = None):
    try:
        print(filter)
        odata_query = filter  # Use the filter parameter to generate the OData query.

        orm_query = select(User)  # This is any form of Query or Selectable.
        query = apply_odata_query(orm_query, odata_query)
        users = db.execute(query).scalars().all()
        print(users)
        return users
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))
