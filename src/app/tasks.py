from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.postgres.database import get_db
from src.postgres import models
from typing import List
from src import schemas


from src.utils import project_utils, task_utils, employee_utils

router = APIRouter(tags=["tasks"])


@router.post("/projects/{project_id}/tasks/", response_model=schemas.TaskGet)
def post_task(
    task: schemas.TaskPost,
    project: models.ProjectModel = Depends(project_utils.get_project_by_id),
    pdb: Session = Depends(get_db),
):
    """Creates a new task"""

    if task.initial_date > project.final_date:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Initial date is greater than final date of project",
        )

    if task.assigned_employee is not None:
        assigned_employee = employee_utils.get_employee_by_id(
            task.assigned_employee, pdb
        )
        task.assigned_employee = assigned_employee

    new_task = models.TaskModel(**task.dict(), project=project)

    pdb.add(new_task)
    pdb.commit()
    pdb.refresh(new_task)

    return new_task


@router.get("/tasks/{task_id}", response_model=schemas.TaskGet)
def get_task(
    task: models.TaskModel = Depends(task_utils.get_task_by_id),
):
    """Get task by id"""

    return task


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

    initial_date = task_update.initial_date or task.initial_date
    final_date = task_update.final_date or task.final_date

    if initial_date > final_date:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Initial date cannot be greater than final date",
        )

    if task_update.assigned_employee is not None:
        assigned_employee = employee_utils.get_employee_by_id(
            task_update.assigned_employee, pdb
        )
        task_update.assigned_employee = assigned_employee

    task_update = task_update.dict(exclude_unset=True)

    for task_attr in task_update:
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
