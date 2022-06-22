from sqlalchemy.orm import Session
from fastapi import Body, Depends
from src.postgres import models
from src.postgres.database import get_db


def get_employee_by_id(employee_id: int, pdb: Session):
    """Returns an employee by its id or 404 if not found"""

    employee = pdb.get(models.EmployeeModel, employee_id)
    if employee is None:
        employee = models.EmployeeModel(id=employee_id)
        pdb.add(employee)
        pdb.commit()

    return employee


def retrieve_employee_by_id(
    employee_id: int = Body(..., embed=True), pdb: Session = Depends(get_db)
):
    """Returns an employee by its id or 404 if not found"""

    return get_employee_by_id(employee_id, pdb)


def retrieve_employee_by_idfrom_path(employee_id: int, pdb: Session = Depends(get_db)):
    """Returns an employee by its id or 404 if not found"""

    return get_employee_by_id(employee_id, pdb)
