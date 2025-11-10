from fastapi import APIRouter, Request

from models.attendance.upload_image import UploadImagePayload

router = APIRouter()


@router.post(
    path="/upload_images"
)
def post_upload_images(request: Request, payload: UploadImagePayload):
    return