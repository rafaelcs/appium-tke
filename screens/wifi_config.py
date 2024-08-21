from appium import webdriver

from screens.base_screen import BaseScreen


class WiFiConfig(BaseScreen):

    def __init__(self, driver):
        super().__init__(driver)

    def toggle_wifi(self):
        self.driver.toggle_wifi()

    def turn_on_wifi(self):
        if not self.is_wifi_on():
            self.toggle_wifi()

    def is_wifi_on(self):
        wifi_status = self.run_adb_shell("dumpsys wifi | grep 'Wi-Fi is'").strip()

        if "Wi-Fi is disabled" in wifi_status:
            return False

        return True
