from pydantic import BaseModel


class EmployeeInfo(BaseModel):
    id: int

    class Config:
        orm_mode = True
