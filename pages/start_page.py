from time import sleep

from constants.start_page import StartPageConstants
from pages.base_page import BasePage


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConstants()

    def sign_in(self, username, password):
        self.fill_field(xpath=self.constants.SIGN_IN_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=password)
        sleep(1)
        self.click(xpath=self.constants.SIGN_IN_PASSWORD_FIELD_XPATH)
        # Click button
        self.click(xpath=self.constants.SIGN_IN_BUTTON_FIELD_XPATH)
        sleep(1)

    def verify_sign_in_error(self):
        assert self.get_element_text(
            self.constants.SIGN_IN_LOGIN_ERROR_FIELD_XPATH) == self.constants.SIGN_IN_LOGIN_ERROR_FIELD_TEXT, \
            f"Actual message: {self.get_element_text(self.constants.SIGN_IN_LOGIN_ERROR_FIELD_XPATH)}"

    def sign_up(self, username, email, password):
        """Sign up as the user"""
        # Fill username
        self.fill_field(xpath=self.constants.SIGN_UP_USERNAME_FIELD_XPATH, value=username)
        self.fill_field(xpath=self.constants.SIGN_UP_EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=password)
        sleep(1)
        # Click button
        self.click(xpath=self.constants.SIGN_UP_BUTTON_FIELD_XPATH)
        sleep(1)

    def verify_success_sign_up(self, username):
        """Verify success Sign Up using hello message"""
        username = username.lower()
        assert self.get_element_text(self.constants.HELLO_MASSAGE_XPATH) == self.constants.HELLO_MASSAGE_TEXT.format(
            username=username), \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MASSAGE_XPATH)}"

        assert self.get_element_text(self.constants.HELLO_MASSAGE_USERNAME_XPATH) == username, \
            f"Actual message: {self.get_element_text(self.constants.HELLO_MASSAGE_USERNAME_XPATH)}"
