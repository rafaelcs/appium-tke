import pytest
from screens.app_screen import AppScreen
import time


class TestInteractWithAdb:

    def test_get_battery_info(self, driver):
        app_screen = AppScreen(driver)
        battery_info = app_screen.run_adb_shell("dumpsys battery")

        print(battery_info)

    def test_get_installed_apps(self, driver):
        app_screen = AppScreen(driver)
        installed_apps = app_screen.run_adb_shell("pm list packages")

        print(installed_apps)
