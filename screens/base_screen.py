from appium import webdriver


class BaseScreen:

    def __init__(self, driver):
        self.driver = driver

    def run_adb_shell(self, command: str) -> str:
        return self.driver.execute_script("mobile: shell", {"command": command})
