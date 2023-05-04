from fastapi import FastAPI
from api.routers import router as api_router
from api.middlewares import apply_cors_middleware


def create_app() -> FastAPI:
    app = FastAPI()
    app = apply_cors_middleware(app)
    app.include_router(api_router, tags=["API"])
    return app