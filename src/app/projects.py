from fastapi import APIRouter, Depends, HTTPException
from src.postgres import schemas
from sqlalchemy.orm import Session
from src.postgres.database import get_db
from src.postgres import models
from typing import List

router = APIRouter(tags=["projects"])


@router.post("/projects/", response_model=schemas.ProjectBase)
def post_project(project: schemas.ProjectPost, pdb: Session = Depends(get_db)):
    """Creates a new project"""

    new_project = models.ProjectModel(**project.dict())

    pdb.add(new_project)
    pdb.commit()
    pdb.refresh(new_project)

    return new_project


@router.get("/projects/", response_model=List[schemas.ProjectBase])
def get_projects(
    pdb: Session = Depends(get_db),
):
    """Returns all projects"""

    projects = pdb.query(models.ProjectModel).all()

    return projects


@router.get("/projects/{project_id}", response_model=schemas.ProjectBase)
def get_project_by_id(project_id: int, pdb: Session = Depends(get_db)):
    """Returns a project by its id or 404 if not found"""

    project = pdb.get(models.ProjectModel, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@router.put("/projects/{project_id}", response_model=schemas.ProjectBase)
def edit_project(
    project_id: int,
    project_update: schemas.ProjectUpdate,
    pdb: Session = Depends(get_db),
):
    """Edits an existing project"""

    project = pdb.get(models.ProjectModel, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    project_update = project_update.dict()

    for project_attr in project_update:
        if project_update[project_attr] is not None:
            setattr(project, project_attr, project_update[project_attr])

    pdb.add(project)
    pdb.commit()

    return project


@router.delete("/projects/{project_id}")
def delete_project(project_id: int, pdb: Session = Depends(get_db)):
    """Deletes an existing project"""

    project = pdb.get(models.ProjectModel, project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    pdb.delete(project)
    pdb.commit()
