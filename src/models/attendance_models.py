from pydantic import BaseModel


class UploadImagesPayload(BaseModel):
    image_paths: list[str]
