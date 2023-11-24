from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from hashing import Hash
from models import User
from schemas import ShowUser, UserIn


async def createUser(request: UserIn, db: Session = Depends(get_db)):
    cekusername = db.query(User).filter(User.username == request.username).first()
    if cekusername:
        raise HTTPException(
            status_code=409,
            detail=f"User with username:{request.username} already exist",
        )

    newuser = User(
        username=request.username,
        email=request.email,
        password=Hash(request.password),
    )
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser


async def getUsers(db: Session = Depends(get_db)):
    stmt = db.query(User).all()
    return [ShowUser.from_orm(x) for x in stmt]


async def getUser(userid: int, db: Session = Depends(get_db)):
    stmt = db.query(User).filter(User.id == userid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"User with id:{userid} is not available"
        )
    return ShowUser.from_orm(stmt)


async def deleteUser(userid: int, db: Session = Depends(get_db)):
    stmt = db.query(User).filter(User.id == userid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"User with id:{userid} is not available"
        )
    db.query(User).filter(User.id == userid).delete(synchronize_session=False)
    db.commit()
    return {"detail": f"User id:{userid} has been deleted"}
