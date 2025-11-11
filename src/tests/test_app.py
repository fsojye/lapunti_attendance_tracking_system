from fastapi import FastAPI

from app import get_app


class TestApp:
    def test_app_should_return_expected_details(self):
        app = get_app()

        assert type(app) is FastAPI
        assert app.title == "Lapunti Attendance Tracking System API"
        assert app.version == "1.0"

    def test_app_routes_when_initialised_should_include_attendance_images_route(
        self, method_path
    ):
        assert ("POST", "/attendance/images") in method_path
