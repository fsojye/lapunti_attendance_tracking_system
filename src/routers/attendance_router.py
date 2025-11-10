from fastapi import APIRouter, Request

from controllers.attendance_post_images_controller import AttendancePostImagesController
from models.attendance_models import UploadImagesPayload

router = APIRouter()


@router.post(path="/images")
def post_images(request: Request, payload: UploadImagesPayload):
    controller = AttendancePostImagesController()
    return controller.execute(payload.image_paths)
