from pydantic.main import BaseModel
from typing import List, Optional
from datetime import date


class TaskBase(BaseModel):
    name: str
    description: str
    initial_date: date
    final_date: date
    estimated_hours: int

    class Config:
        orm_mode = True


class TaskUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    initial_date: Optional[date]
    final_date: Optional[date]
    estimated_hours: Optional[int]

    class Config:
        orm_mode = True


class ProjectInfo(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class TaskGet(TaskBase):
    id: int
    project: ProjectInfo


class TaskPost(TaskBase):
    initial_date: date
    final_date: date
    estimated_hours: int

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "name": "Actualizar dependencias del proyecto",
                "description": "Se deben solucionar todos los conflictos existentes entre las"
                "dependencias del proyecto",
                "initial_date": "2020-05-02",
                "final_date": "2020-06-26",
                "estimated_hours": 100,
            }
        }


class ProjectPost(BaseModel):
    name: str
    initial_date: date
    final_date: date
    estimated_hours: int

    class Config:
        orm_mode = True

        schema_extra = {
            "example": {
                "name": "PSA Spring ERP V1.0",
                "initial_date": "2020-01-01",
                "final_date": "2020-06-25",
                "estimated_hours": 150,
            }
        }


class TaskGetProject(BaseModel):
    id: int
    name: str
    description: str
    initial_date: date
    final_date: date
    estimated_hours: int

    class Config:
        orm_mode = True


class ProjectBase(ProjectPost):
    id: int
    tasks: Optional[List[TaskGetProject]]

    class Config:
        orm_mode = True


class ProjectUpdate(BaseModel):
    name: Optional[str]
    initial_date: Optional[date]
    final_date: Optional[date]
    estimated_hours: Optional[int]

    class Config:
        orm_mode = True
