from sqlalchemy.orm import Session
from fastapi import HTTPException, Body, Depends
from src.postgres import models
from src.postgres.database import get_db


def get_employee_by_id(employee_id: str, pdb: Session):
    """Returns an employee by its id or 404 if not found"""

    employee = pdb.get(models.EmployeeModel, employee_id)
    if employee is None:
        employee = models.EmployeeModel(id=employee_id)

    return employee


def retrieve_employee_by_id(
    employee_id: str = Body("105836", embed=True), pdb: Session = Depends(get_db)
):
    """Returns an employee by its id or 404 if not found"""

    return get_employee_by_id(employee_id, pdb)
