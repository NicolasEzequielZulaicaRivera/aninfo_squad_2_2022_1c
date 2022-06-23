from typing import Optional, Type, List
from fastapi import Depends, Body, HTTPException, status

from .employee import EmployeeInfo
from .resource import ResourcePost, ResourceUpdate, ResourceGet, ResourceInfo
from src.postgres.database import get_db
from sqlalchemy.orm import Session

from ..postgres.models import ResourceModel
from ..utils.task_utils import get_task_by_id


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


class TaskUpdate(ResourceUpdate, TaskExample):
    estimated_hours: Optional[int] = Body(None, ge=0)


class TaskGet(ResourceGet):
    from .project import ProjectInfo

    project: ProjectInfo
    assigned_employee: Optional[EmployeeInfo]
    collaborators: List[EmployeeInfo]
    estimated_hours: Optional[int]
