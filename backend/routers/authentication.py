from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import get_db
from hashing import Verify
from models import User
from schemas import Token
from tokenize import create_access_token

router = APIRouter(tags=["Authentication"])


@router.post("/login", status_code=202, response_model=Token)
def login(
    request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=401,
            detail=f"User with email:{request.username} not exist",
        )
    passw_verif = Verify(request.password, user.password)
    if not passw_verif:
        raise HTTPException(
            status_code=401,
            detail="invalid credentials",
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
