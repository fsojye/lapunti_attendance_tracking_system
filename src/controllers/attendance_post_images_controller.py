class AttendancePostImagesController:
    def __init__(
        self,
        image_validation_service=None,
        file_compression_service=None,
        file_storage_service=None,
    ):
        self._image_validation_service = image_validation_service
        self._file_compression_service = file_compression_service
        self._file_storage_service = file_storage_service

    def execute(self, image_paths: list[str]) -> str:
        return self.__execute(image_paths)

    def __execute(self, image_paths: list[str]) -> str:
        return ", ".join(image_paths)
