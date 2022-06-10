from pydantic.main import BaseModel
from typing import List, Optional
from datetime import datetime


class TaskBase(BaseModel):
    name: str
    description: str
    initial_date: datetime
    final_date: datetime
    estimated_hours: int

    class Config:
        orm_mode = True


class TaskUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    initial_date: Optional[datetime]
    final_date: Optional[datetime]
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
    initial_date: datetime
    final_date: datetime
    estimated_hours: int

    class Config:
        orm_mode = True


class ProjectPost(BaseModel):
    name: str
    initial_date: datetime
    final_date: datetime
    estimated_hours: int

    class Config:
        orm_mode = True


class TaskGetProject(BaseModel):
    id: int
    name: str
    description: str
    initial_date: datetime
    final_date: datetime
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
    initial_date: Optional[datetime]
    final_date: Optional[datetime]
    estimated_hours: Optional[int]

    class Config:
        orm_mode = True
