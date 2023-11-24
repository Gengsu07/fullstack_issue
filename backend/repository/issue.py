from fastapi import Depends, HTTPException
from sqlalchemy import update
from sqlalchemy.orm import Session

from database import get_db
from models import Issue
from schemas import IssueBase, IssueIn


def getIssues(db: Session = Depends(get_db)):
    issues = db.query(Issue).all()
    return [IssueBase.from_orm(x) for x in issues]


def getIssue(issueid: int, db: Session = Depends(get_db)):
    stmt = db.query(Issue).filter(Issue.id == issueid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"Issue with id:{issueid} is not available"
        )
    return IssueBase.from_orm(stmt)


def createIssue(issue: IssueIn, db: Session = Depends(get_db)):
    newissue = Issue(title=issue.title, description=issue.description, user_id=2)
    db.add(newissue)
    db.commit()
    db.refresh(newissue)
    return newissue


def deleteIssue(issueid: int, db: Session = Depends(get_db)):
    stmt = db.query(Issue).filter(Issue.id == issueid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"Issue with id:{issueid} is not available"
        )
    db.query(Issue).filter(Issue.id == issueid).delete(synchronize_session=False)
    # del_stmt = delete(Issue).where(Issue.id == issueid)
    # db.execute(del_stmt)
    db.commit()
    return {"Detail": f"Data with id:{issueid} has been deleted"}


def updateIssue(issueid: int, request: IssueIn, db: Session = Depends(get_db)):
    stmt = db.query(Issue).filter(Issue.id == issueid).first()
    if not stmt:
        raise HTTPException(
            status_code=404, detail=f"Issue with id:{issueid} is not available"
        )
    stmt_update = (
        update(Issue)
        .where(Issue.id == issueid)
        .values(title=request.title, description=request.description)
    )
    db.execute(stmt_update)
    db.commit()
    return "updated"
