from sqlalchemy.orm import Session

from . import models, schemas


def create_new_issue(db: Session, issue_in: schemas.IssueIn):
    # Create a new Issue instance using the data provided in issue_in
    new_issue = models.Issue(title=issue_in.title, description=issue_in.description)

    # Add the new issue to the database
    db.add(new_issue)
    db.commit()

    # Refresh the session to ensure we have the latest data (including the generated ID)
    db.refresh(new_issue)

    # Return the newly created issue
    return new_issue
