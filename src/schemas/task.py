from typing import Optional, List, Any
from fastapi import Body
from pydantic.utils import GetterDict

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
    assigned_employee: Optional[int] = Body(None)

    @staticmethod
    def valid_states():
        return STATES


class TaskUpdate(ResourceUpdate, TaskExample):
    estimated_hours: Optional[int] = Body(None, ge=0)
    assigned_employee: Optional[int] = Body(None)

    @staticmethod
    def valid_states() -> List[str]:
        return STATES


class ProjectInfo(ResourceInfo):
    id: int
    name: str

    class Config:
        orm_mode = True


class TaskGetter(GetterDict):
    def get(self, key: Any, default: Any = None) -> Any:
        if key == "assigned_employee":
            if self._obj.assigned_employee is None:
                return None
            return self._obj.assigned_employee.id
        else:
            try:
                return getattr(self._obj, key)
            except (AttributeError, KeyError):
                return default


class TaskGet(ResourceGet):
    project: ProjectInfo
    assigned_employee: Optional[int]
    collaborators: List[EmployeeInfo]
    estimated_hours: Optional[int]

    class Config:
        getter_dict = TaskGetter


class TaskGetProjectById(ResourceGet):
    assigned_employee: Optional[int]
    collaborators: List[EmployeeInfo]
    estimated_hours: Optional[int]

    class Config:
        getter_dict = TaskGetter
