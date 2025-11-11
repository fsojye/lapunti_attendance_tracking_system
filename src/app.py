from fastapi import FastAPI

from routers import attendance_router


def get_app() -> FastAPI:
    app = FastAPI(
        title="Lapunti Attendance Tracking System API",
        version=_get_version(),
    )

    app.include_router(
        attendance_router.router,
        prefix="/attendance",
        tags=["Attendance"],
    )

    return app


def _get_version() -> str:
    return "1.0"
