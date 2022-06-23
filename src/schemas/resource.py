from datetime import date
from pydantic import BaseModel, validator
from typing import Optional
from fastapi import HTTPException, status


class ResourceInfo(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ResourcePost(BaseModel):
    name: str
    description: str
    initial_date: date
    final_date: date

    @validator("final_date")
    def validate_final_date(cls, v, values):  # pylint: disable=no-self-argument,no-self-use
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
    finished: Optional[bool]

    class Config:
        orm_mode = True


class ResourceGet(ResourcePost):
    id: int
    finished: bool
