from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

from src.postgres import models
from src.postgres.database import get_db


def get_task_by_id(task_id: int, pdb: Session = Depends(get_db)):
    task = pdb.get(models.TaskModel, task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task
