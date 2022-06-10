from src.postgres import models
from src.postgres.database import get_db
from fastapi import Depends, HTTPException, status


def get_project_by_id(project_id: int, pdb=Depends(get_db)):
    project = pdb.get(models.ProjectModel, project_id)
    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )
    return project
