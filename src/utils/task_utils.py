from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session
from datetime import date
from fastapi import Body
from typing import Optional

from src.postgres import models, schemas
from src.postgres.database import get_db


def get_task_by_id(task_id: int, pdb: Session = Depends(get_db)):
    task = pdb.get(models.TaskModel, task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )
    return task


def retrieve_task_post(
    name: str = Body(..., embed=True),
    description: str = Body(..., embed=True),
    initial_date: date = Body(..., embed=True),
    final_date: date = Body(..., embed=True),
    estimated_hours: Optional[int] = Body(..., ge=0, embed=True),
) -> schemas.TaskBase:
    if initial_date > final_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Initial date must be before final date",
        )

    return schemas.TaskBase(
        name=name,
        description=description,
        initial_date=initial_date,
        final_date=final_date,
        estimated_hours=estimated_hours,
    )


def retrieve_task_update(
    name: Optional[str] = Body(None, embed=True),
    description: Optional[str] = Body(None, embed=True),
    initial_date: Optional[date] = Body(None, embed=True),
    final_date: Optional[date] = Body(None, embed=True),
    estimated_hours: Optional[int] = Body(None, ge=0, embed=True),
):
    if initial_date > final_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Initial date must be before final date",
        )

    return schemas.TaskBase(
        name=name,
        description=description,
        initial_date=initial_date,
        final_date=final_date,
        estimated_hours=estimated_hours,
    )
