from fastapi import APIRouter, Depends, HTTPException, status
from src import schemas
from sqlalchemy.orm import Session
from src.postgres.database import get_db
from src.postgres import models
from src import utils
from typing import List

from src.utils import project_utils

router = APIRouter(tags=["projects"])


@router.post("/projects/", response_model=schemas.ProjectGet)
def post_project(
    project: schemas.ProjectPost,
    pdb: Session = Depends(get_db),
):
    """Creates a new project"""
    new_project = models.ProjectModel(**project.dict())

    pdb.add(new_project)
    pdb.commit()
    pdb.refresh(new_project)

    return new_project


@router.get("/projects/", response_model=List[schemas.ProjectGet])
def get_projects(
    pdb: Session = Depends(get_db),
):
    """Returns all projects"""

    projects = pdb.query(models.ProjectModel).all()

    return projects


@router.get("/projects/{project_id}", response_model=schemas.ProjectGet)
def get_project_by_id(project_id: int, pdb: Session = Depends(get_db)):
    """Returns a project by its id or 404 if not found"""

    project = pdb.get(models.ProjectModel, project_id)
    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )

    return project


@router.put("/projects/{project_id}", response_model=schemas.ProjectGet)
def edit_project(
    project_update: schemas.ProjectUpdate,
    project: models.ProjectModel = Depends(project_utils.get_project_by_id),
    pdb: Session = Depends(get_db),
):
    """Edits an existing project"""

    initial_date = project_update.initial_date or project.initial_date
    final_date = project_update.final_date or project.final_date

    if initial_date > final_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Initial date must be before final date",
        )

    if project_update.finished is True and project.finished is True:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Project already finished",
        )
    if project_update.finished is True and any(task.finished is False for task in project.tasks):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Project cannot be finished until all tasks are finished",
        )

    project_update = project_update.dict(exclude_unset=True)
    for project_attr in project_update:
        setattr(project, project_attr, project_update[project_attr])

    pdb.add(project)
    pdb.commit()

    return project


@router.delete("/projects/{project_id}")
def delete_project(project_id: int, pdb: Session = Depends(get_db)):
    """Deletes an existing project"""

    project = pdb.get(models.ProjectModel, project_id)
    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    pdb.delete(project)
    pdb.commit()
