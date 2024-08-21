import pytest
from screens.wifi_config import WiFiConfig


class TestWifi:

    @pytest.fixture(autouse=True)
    def turn_on_wifi(self, driver):
        wifi_config = WiFiConfig(driver)
        wifi_config.turn_on_wifi()
        yield
        wifi_config.turn_on_wifi()

    def test_turn_off_wifi(self, driver):
        wifi_config = WiFiConfig(driver)

        if wifi_config.is_wifi_on():
            wifi_config.toggle_wifi()
            assert (
                not wifi_config.is_wifi_on()
            ), "O Wi-Fi deve estar desligado no final do teste"
