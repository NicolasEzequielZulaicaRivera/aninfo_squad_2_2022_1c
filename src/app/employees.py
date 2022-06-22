from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.postgres.database import get_db
from src.postgres import models, schemas

from src.utils import task_utils, employee_utils

router = APIRouter(tags=["employees"])


@router.post("/tasks/{task_id}/employees/")
def assign_employee_to_task(
    task: models.TaskModel = Depends(task_utils.get_task_by_id),
    employee: models.EmployeeModel = Depends(employee_utils.retrieve_employee_by_id),
    pdb: Session = Depends(get_db),
):
    """Assignates an employee to a task. The employee is responsible for the task."""

    if task.assigned_employee is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Task already assigned to employee with id {task.assigned_employee.id}",
        )

    task.assigned_employee = employee
    pdb.commit()


@router.delete("/tasks/{task_id}/employees/")
def unassign_employee_from_task(
    task: models.TaskModel = Depends(task_utils.get_task_by_id),
    pdb: Session = Depends(get_db),
):
    """Unassignates an employee from a task. The employee is no longer responsible for the task."""

    if task.assigned_employee is None:
        raise HTTPException(status_code=400, detail="Task not assigned to any employee")

    assigned_employee = task.assigned_employee

    if len(assigned_employee.tasks) == 1:
        pdb.delete(assigned_employee)
    else:
        task.assigned_employee = None
    pdb.commit()


@router.post("/tasks/{task_id}/collaborators/", response_model=schemas.EmployeeInfo)
def add_collaborator_to_task(
    task: models.TaskModel = Depends(task_utils.get_task_by_id),
    employee: models.EmployeeModel = Depends(employee_utils.retrieve_employee_by_id),
    pdb: Session = Depends(get_db),
):
    """Adds a collaborator to a task. The collaborator can charge hours to the task through the resources module"""

    if employee in task.collaborators:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Employee with id {employee.id} is already a collaborator of this task",
        )

    task.collaborators.append(employee)
    pdb.commit()
    return employee


@router.delete("/tasks/{task_id}/collaborators/{employee_id}")
def remove_collaborator_from_task(
    task: models.TaskModel = Depends(task_utils.get_task_by_id),
    employee: models.EmployeeModel = Depends(
        employee_utils.retrieve_employee_by_idfrom_path
    ),
    pdb: Session = Depends(get_db),
):
    """Removes a collaborator from a task."""

    if employee not in task.collaborators:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Employee with id {employee.id} is not a collaborator of this task",
        )

    task.collaborators.remove(employee)
    pdb.commit()
