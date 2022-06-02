from fastapi import FastAPI, Depends
from src.app import projects, tasks
from src.middleware.utils import get_api_key
from src.postgres.database import Base, engine

API_VERSION_PREFIX = "/api/v1"

app = FastAPI(
    title="Projects API",
    description="API to manage projects module",
    version="0.0.1",
    dependencies=[Depends(get_api_key)],
)


Base.metadata.drop_all(engine)
Base.metadata.create_all(bind=engine)

app.include_router(projects.router, prefix=API_VERSION_PREFIX)
app.include_router(tasks.router, prefix=API_VERSION_PREFIX)
