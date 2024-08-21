from screens.base_screen import BaseScreen


class AppScreen(BaseScreen):
    def __init__(self, driver):
        super().__init__(driver)

    def is_app_installed(self, app_id):
        return self.driver.is_app_installed(app_id)
