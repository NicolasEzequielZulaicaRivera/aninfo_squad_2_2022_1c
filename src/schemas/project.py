from typing import List
from .task import TaskInfo
from src.schemas.resource import ResourcePost, ResourceUpdate, ResourceGet, ResourceInfo


class ProjectPostExample:
    class Config:
        schema_extra = {
            "example": {
                "name": "PSA Spring ERP V1.0",
                "description": "Este proyecto nos permitirá aumentar los ingresos en un 20%",
                "initial_date": "2020-01-01",
                "final_date": "2020-06-25",
            }
        }


class ProjectGetExample:
    class Config:
        schema_extra = {
            "example": {
                "id": 25,
                "name": "PSA Spring ERP V1.0",
                "description": "Este proyecto nos permitirá aumentar los ingresos en un 20%",
                "initial_date": "2020-01-01",
                "final_date": "2020-06-25",
            }
        }


class ProjectInfo(ResourceInfo):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProjectPost(ResourcePost, ProjectPostExample):
    pass


class ProjectUpdate(ResourceUpdate, ProjectPostExample):
    pass


class ProjectGet(ResourceGet, ProjectGetExample):
    tasks: List[TaskInfo]
