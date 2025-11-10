from pydantic import BaseModel


class UploadImagePayload(BaseModel):
    image_paths: list[str]