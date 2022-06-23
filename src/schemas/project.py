from typing import List
from src.schemas.resource import ResourcePost, ResourceUpdate, ResourceGet
from src.schemas.task import TaskGetProjectById


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


class ProjectPost(ResourcePost, ProjectPostExample):
    pass


class ProjectUpdate(ResourceUpdate, ProjectPostExample):
    pass


class ProjectGet(ResourceGet, ProjectGetExample):
    from .task import TaskInfo

    tasks: List[TaskInfo]


class ProjectGetById(ResourceGet):
    from .task import TaskGet

    tasks: List[TaskGetProjectById]
