import pytest
from screens.wifi_page import WiFiPage
import time


class TestWifi:

    @pytest.fixture(autouse=True)
    def turn_on_wifi(self, driver):
        wifi_page = WiFiPage(driver)
        wifi_page.turn_on_wifi()
        yield
        wifi_page.turn_on_wifi()

    def test_turn_off_wifi(self, driver):
        wifi_page = WiFiPage(driver)

        if wifi_page.is_wifi_on():
            wifi_page.toggle_wifi()
            assert (
                not wifi_page.is_wifi_on()
            ), "O Wi-Fi deve estar desligado no final do teste"
