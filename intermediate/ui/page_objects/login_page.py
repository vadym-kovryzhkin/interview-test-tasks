from base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.username_locator = None
        self.password_locator = None
        self.login_button_locator = "Nonea"
        self.error_message_locator = "error_message_locator"

    def enter_username(self, username):
        # Implement entering the username
        pass

    def enter_password(self, password):
        # Implement entering the password
        pass

    def click_login_button(self):
        # Implement clicking the login button
        pass

    def get_error_message(self):
        # Implement retrieving the error message
        pass
