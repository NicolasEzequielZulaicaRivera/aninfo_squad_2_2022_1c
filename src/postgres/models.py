from sqlalchemy import Column, ForeignKey, Integer, String, Table, Date, Boolean
from sqlalchemy.orm import relationship

from src.postgres.database import Base

task_collaborators_association_table = Table(
    "task_collaborators_association",
    Base.metadata,
    Column("task_id", Integer, ForeignKey("tasks.id"), primary_key=True),
    Column("employee_id", Integer, ForeignKey("employees.id"), primary_key=True),
)


class ResourceModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    initial_date = Column(Date, nullable=False)
    final_date = Column(Date, nullable=False)
    state = Column(String, nullable=False)


class ProjectModel(ResourceModel):
    __tablename__ = "projects"

    tasks = relationship(
        "TaskModel", back_populates="project", cascade="all, delete-orphan"
    )


class TaskModel(ResourceModel):
    __tablename__ = "tasks"

    estimated_hours = Column(Integer, nullable=True)

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
    collaborators = relationship(
        "EmployeeModel",
        secondary=task_collaborators_association_table,
        back_populates="tasks",
    )


class EmployeeModel(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    assigned_tasks = relationship(
        "TaskModel", back_populates="assigned_employee", cascade="all, delete-orphan"
    )
    tasks = relationship("TaskModel", secondary=task_collaborators_association_table)
