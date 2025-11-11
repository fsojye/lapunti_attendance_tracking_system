import pytest
from fastapi.routing import APIRoute

from app import get_app


@pytest.fixture()
def method_path() -> list[tuple[str, str]]:
    app = get_app()
    return [
        (",".join(r.methods), r.path) for r in app.routes if isinstance(r, APIRoute)
    ]
