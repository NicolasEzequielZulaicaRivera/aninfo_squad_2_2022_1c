from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import Table

from src.postgres.database import Base


class ProjectModel(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    initial_date = Column(DateTime, nullable=False)
    final_date = Column(DateTime, nullable=False)
    estimated_hours = Column(Integer, nullable=False)

    tasks = relationship("TaskModel", back_populates="project")


class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    project_id = Column(
        Integer,
        ForeignKey("projects.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    project = relationship("ProjectModel", back_populates="tasks")
