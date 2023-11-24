from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from oauth import get_current_user
from repository.user import createUser, deleteUser, getUser, getUsers
from schemas import ShowUser, UserIn

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", status_code=201, response_model=ShowUser)
async def create_user(
    request: UserIn,
    db: Session = Depends(get_db),
    current_user: UserIn = Depends(get_current_user),
):
    return await createUser(request, db)


@router.get("/", status_code=200, response_model=List[ShowUser])
async def get_users(
    db: Session = Depends(get_db), current_user: UserIn = Depends(get_current_user)
):
    return await getUsers(db)


@router.get("/{userid}", status_code=200, response_model=ShowUser)
async def get_user(
    userid: int,
    db: Session = Depends(get_db),
    current_user: UserIn = Depends(get_current_user),
):
    return await getUser(userid, db)


@router.delete("/{userid}", status_code=204)
async def del_user(
    userid: int,
    db: Session = Depends(get_db),
    current_user: UserIn = Depends(get_current_user),
):
    return await deleteUser(userid, db)
