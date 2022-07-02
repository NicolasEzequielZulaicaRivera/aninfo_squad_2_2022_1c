from abc import ABC, abstractmethod
from datetime import date
from pydantic import BaseModel, validator
from typing import Optional, List
from fastapi import HTTPException, status

COMMON_STATES = ["sin iniciar", "en progreso"]


class ResourceInfo(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ResourcePost(BaseModel, ABC):
    name: str
    description: str
    initial_date: date
    final_date: date
    state: str = "sin iniciar"

    @staticmethod
    @abstractmethod
    def valid_states() -> List[str]:
        pass

    @validator("state")
    def validate_state(
        cls, v, values
    ):  # pylint: disable=unused-argument, no-self-argument
        if v not in cls.valid_states():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="State must be one of: {}".format(", ".join(cls.valid_states())),
            )
        return v

    @validator("final_date")
    def validate_final_date(
        cls, v, values
    ):  # pylint: disable=no-self-argument,no-self-use
        if values["initial_date"] > v:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Initial date must be before final date",
            )
        return v

    class Config:
        orm_mode = True


class ResourceUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    initial_date: Optional[date]
    final_date: Optional[date]
    state: Optional[str]

    @staticmethod
    @abstractmethod
    def valid_states() -> List[str]:
        pass

    @validator("state")
    def validate_state(
        cls, v, values
    ):  # pylint: disable=unused-argument, no-self-argument
        if v not in cls.valid_states():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="State must be one of: {}".format(", ".join(cls.valid_states())),
            )
        return v

    class Config:
        orm_mode = True


class ResourceGet(BaseModel):
    id: int
    name: str
    description: str
    initial_date: date
    final_date: date
    state: str

    class Config:
        orm_mode = True
