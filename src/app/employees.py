from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.postgres.database import get_db
from src.postgres import models
from typing import List
from src.postgres import schemas


from src.utils import project_utils, task_utils, employee_utils

router = APIRouter(tags=["employees"])


@router.post("/tasks/{task_id}/employees/")
def assign_employee_to_task(
    task: models.TaskModel = Depends(task_utils.get_task_by_id),
    employee: models.EmployeeModel = Depends(employee_utils.retrieve_employee_by_id),
    pdb: Session = Depends(get_db),
):
    """Assignates an employee to a task"""

    if task.assigned_employee is not None:
        raise HTTPException(
            status_code=400,
            detail=f"Task already assigned to employee with id {task.assigned_employee.id}",
        )

    task.assigned_employee = employee
    pdb.add(task)
    pdb.commit()


@router.delete("/tasks/{task_id}/employees/")
def unassign_employee_from_task(
    task: models.TaskModel = Depends(task_utils.get_task_by_id),
    pdb: Session = Depends(get_db),
):
    """Unassignates an employee from a task"""

    if task.assigned_employee is None:
        raise HTTPException(status_code=400, detail="Task not assigned to any employee")

    assigned_employee = task.assigned_employee

    task.assigned_employee = None
    if not task.assigned_employee:
        pdb.delete(assigned_employee)
    pdb.add(task)
    pdb.commit()
