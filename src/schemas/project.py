from typing import List
from src.schemas.resource import (
    ResourcePost,
    ResourceUpdate,
    ResourceGet,
    COMMON_STATES,
)
from src.schemas.task import TaskGetProjectById


STATES = COMMON_STATES
STATES += ["cancelado", "bloqueado", "finalizado"]


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
    @staticmethod
    def valid_states():
        return STATES


class ProjectUpdate(ResourceUpdate, ProjectPostExample):
    @staticmethod
    def valid_states() -> List[str]:
        return STATES


class ProjectGet(ResourceGet, ProjectGetExample):
    collaborators_amount: int
    tasks_amount: int


class ProjectGetById(ResourceGet):
    tasks: List[TaskGetProjectById]
