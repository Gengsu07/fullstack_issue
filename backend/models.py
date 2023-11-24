from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Issue(Base):
    __tablename__ = "issue"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    createdAt = Column(DateTime, default=datetime.now())
    user_id: int = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="issues")


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    createdAt = Column(DateTime, default=datetime.now())
    issues = relationship("Issue", back_populates="user")
