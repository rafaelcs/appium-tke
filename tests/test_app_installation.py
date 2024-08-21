import pytest
from screens.app_screen import AppScreen


class TestAppInstalation:
    def test_install_app(self, driver):
        app_page = AppScreen(driver)
        expected_app_id = "org.simple.clinic.staging"

        assert app_page.is_app_installed(
            expected_app_id
        ), "O app deveria estar instalado"
