from fastapi import APIRouter, Depends, HTTPException
from src.postgres import schemas
from sqlalchemy.orm import Session
from src.postgres.database import get_db
from src.postgres import models
from typing import List

router = APIRouter(tags=["tasks"])
