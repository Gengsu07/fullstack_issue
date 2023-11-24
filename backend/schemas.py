from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class IssueIn(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class UserIn(BaseModel):
    username: str
    email: Optional[str]
    password: str


class UserBase(UserIn):
    id: int
    createdAt: Optional[datetime]

    class Config:
        orm_mode = True


class UserMini(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    username: str
    email: str
    issues: List[IssueIn]

    class Config:
        orm_mode = True


class IssueBase(IssueIn):
    id: int
    createdAt: Optional[datetime]
    user: UserMini

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
