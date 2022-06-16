from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.postgres.database import Base


class ProjectModel(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    initial_date = Column(DateTime, nullable=False)
    final_date = Column(DateTime, nullable=False)
    estimated_hours = Column(Integer, nullable=False)

    tasks = relationship(
        "TaskModel", back_populates="project", cascade="all, delete-orphan"
    )


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)

    initial_date = Column(DateTime, nullable=False)
    final_date = Column(DateTime, nullable=False)
    estimated_hours = Column(Integer, nullable=False)

    project_id = Column(
        Integer,
        ForeignKey("projects.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    project = relationship("ProjectModel", back_populates="tasks")
    assigned_employee_id = Column(
        Integer,
        ForeignKey("employees.id", ondelete="SET NULL", onupdate="CASCADE"),
        nullable=True,
    )
    assigned_employee = relationship("EmployeeModel", back_populates="tasks")


class EmployeeModel(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    tasks = relationship("TaskModel", back_populates="assigned_employee")
