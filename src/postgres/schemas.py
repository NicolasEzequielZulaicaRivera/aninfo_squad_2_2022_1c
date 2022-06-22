from pydantic import validator
from pydantic.main import BaseModel
from typing import List, Optional
from datetime import date
from fastapi import Body, HTTPException, status


class TaskBase(BaseModel):
    name: str
    description: str
    initial_date: date
    final_date: date
    estimated_hours: Optional[int] = Body(None, ge=0)

    @validator("final_date")
    def check_dates(cls, v, values):
        if "initial_date" in values and values["initial_date"] > v:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Initial date must be before final date",
            )
        return v

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "name": "Actualizar dependencias del proyecto",
                "description": "Se deben solucionar todos los conflictos existentes entre las"
                "dependencias del proyecto",
                "initial_date": "2020-05-02",
                "final_date": "2020-06-26",
            }
        }


class TaskUpdate(TaskBase):
    name: Optional[str]
    description: Optional[str]
    initial_date: Optional[date]
    final_date: Optional[date]
    estimated_hours: Optional[int] = Body(None, ge=0)


class ProjectInfo(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class EmployeeInfo(BaseModel):
    id: int

    class Config:
        orm_mode = True


class TaskGet(TaskBase):
    id: int
    project: ProjectInfo
    assigned_employee: Optional[EmployeeInfo]
    collaborators: List[EmployeeInfo]


class ProjectBase(BaseModel):
    name: str
    description: str
    initial_date: date
    final_date: date

    @validator("final_date")
    def check_dates(cls, v, values):
        if "initial_date" in values and values["initial_date"] > v:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Initial date must be before final date",
            )
        return v

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "name": "PSA Spring ERP V1.0",
                "description": "Este proyecto nos permitirá aumentar los ingresos en un 20%",
                "initial_date": "2020-01-01",
                "final_date": "2020-06-25",
            }
        }


class ProjectGet(ProjectBase):
    id: int
    tasks: Optional[List[TaskGet]]


class ProjectUpdate(ProjectBase):
    name: Optional[str]
    description: Optional[str]
    initial_date: Optional[date]
    final_date: Optional[date]
