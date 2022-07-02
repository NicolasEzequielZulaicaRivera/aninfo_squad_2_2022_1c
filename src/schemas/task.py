from typing import Optional, List
from fastapi import Body

from .employee import EmployeeInfo
from .resource import (
    ResourcePost,
    ResourceUpdate,
    ResourceGet,
    ResourceInfo,
    COMMON_STATES,
)


STATES = COMMON_STATES
STATES += [
    "cancelada",
    "bloqueada",
    "iniciada",
    "finalizada",
]


class TaskExample:
    class Config:
        schema_extra = {
            "example": {
                "name": "Actualizar dependencias del proyecto",
                "description": "Se deben solucionar todos los conflictos existentes entre las"
                "dependencias del proyecto",
                "initial_date": "2020-05-02",
                "final_date": "2020-06-26",
            }
        }


class TaskInfo(ResourceInfo):
    pass


class TaskPost(ResourcePost, TaskExample):
    estimated_hours: Optional[int] = Body(None, ge=0)

    @staticmethod
    def valid_states():
        return STATES


class TaskUpdate(ResourceUpdate, TaskExample):
    estimated_hours: Optional[int] = Body(None, ge=0)

    @staticmethod
    def valid_states() -> List[str]:
        return STATES


class ProjectInfo(ResourceInfo):
    id: int
    name: str

    class Config:
        orm_mode = True


class TaskGet(ResourceGet):
    project: ProjectInfo
    assigned_employee: Optional[EmployeeInfo]
    collaborators: List[EmployeeInfo]
    estimated_hours: Optional[int]


class TaskGetProjectById(ResourceGet):
    assigned_employee: Optional[EmployeeInfo]
    collaborators: List[EmployeeInfo]
    estimated_hours: Optional[int]
