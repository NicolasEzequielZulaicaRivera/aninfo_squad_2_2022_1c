from fastapi import FastAPI
from src.app import projects, tasks
from src.middleware.middleware import apply_middleware

API_VERSION_PREFIX = "/api/v1"

app = FastAPI(
    title="Projects API", description="API to manage projects module", version="0.0.1"
)

apply_middleware(app)

app.include_router(projects.router, prefix=API_VERSION_PREFIX)
app.include_router(tasks.router, prefix=API_VERSION_PREFIX)
