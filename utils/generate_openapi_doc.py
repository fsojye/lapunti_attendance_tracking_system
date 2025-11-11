import json

from fastapi.openapi.utils import get_openapi

from src.app import get_app

app = get_app()

doc = json.dumps(
    get_openapi(
        title=app.title,
        version=app.version,
        openapi_version=app.openapi_version,
        description=app.description,
        routes=app.routes,
    ),
    indent=2,
)

print(doc)
