from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.postgres.database import get_db
from src.postgres import models
from typing import List
from src.postgres import schemas


from src.utils import project_utils, task_utils

router = APIRouter(tags=["tasks"])


@router.post("/projects/{project_id}/tasks/", response_model=schemas.TaskGet)
def post_task(
    task: schemas.TaskPost,
    project: models.ProjectModel = Depends(project_utils.get_project_by_id),
    pdb: Session = Depends(get_db),
):
    """Creates a new task"""

    new_task = models.TaskModel(**task.dict(), project=project)

    pdb.add(new_task)
    pdb.commit()
    pdb.refresh(new_task)

    return new_task


@router.get("/tasks/", response_model=List[schemas.TaskGet])
def get_tasks(pdb: Session = Depends(get_db)):
    """Returns all tasks"""

    return pdb.query(models.TaskModel).all()


@router.put("/tasks/{task_id}", response_model=schemas.TaskGet)
def edit_task(
    task_update: schemas.TaskUpdate,
    task: models.TaskModel = Depends(task_utils.get_task_by_id),
    pdb: Session = Depends(get_db),
):
    """Edits an existing task"""

    task_update = task_update.dict()

    for task_attr in task_update:
        if task_update[task_attr] is not None:
            setattr(task, task_attr, task_update[task_attr])

    pdb.add(task)
    pdb.commit()
    pdb.refresh(task)

    return task


@router.delete("/tasks/{task_id}")
def delete_task(
    task: models.TaskModel = Depends(task_utils.get_task_by_id),
    pdb: Session = Depends(get_db),
):
    """Deletes an existing task"""

    pdb.delete(task)
    pdb.commit()
