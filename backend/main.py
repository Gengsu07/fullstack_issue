from fastapi import FastAPI

import models

from database import engine
from routers.authentication import router as LoginRouter
from routers.issueAPI import router as IssueRouter
from routers.userAPI import router as UserRouter

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gengsu Tracker Issue")

app.include_router(LoginRouter)
app.include_router(IssueRouter)
app.include_router(UserRouter)
