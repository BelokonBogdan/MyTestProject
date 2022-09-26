import logging

import pytest
from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL
from pages.start_page import StartPage
from pages.utils import random_str, random_num


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @pytest.fixture(scope="function")
    def start_page(self):
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        yield StartPage(driver)
        driver.close()

    def test_incorrect_login(self, start_page):
        """
        - Create driver
        - Open page
        - Enter fake login
        - Enter fake password
        - Click button
        - Verify error
        """
        start_page.sign_in("User1", "1111")
        self.log.info("Logged")

        start_page.verify_sign_in_error()
        self.log.info("Verified")

    def test_empty_login(self, start_page):
        """
        - Create driver
        - Open page
        - Clear login
        - Clear password
        - Click button
        - Verify error
        """
        start_page.sign_in("", "")
        self.log.info("Logged")

        start_page.verify_sign_in_error()
        self.log.info("Verified")

    def test_symbols_ascii(self, start_page):
        """
        - Create driver
        - Open page
        - Enter fake-ascii login
        - Enter fake password with ascii
        - Click button
        - Verify error
        """
        start_page.sign_in("♣☺♂", "♣☺♂123456789")
        self.log.info("Logged")

        start_page.verify_sign_in_error()
        self.log.info("Verified")

    def test_valid_login(self, start_page):
        """
        - Create driver
        - Open page
        - Enter valid login
        - Enter valid password
        - Click button
        - Verify login is successful
        """
        username = "testuser"
        start_page.sign_in(username, "qwe123456789")
        self.log.info("Logged")

        start_page.verify_success_sign_up(username)
        self.log.info("Verified")

    def test_valid_registration(self, start_page):
        """
        - Create driver
        - Open page
        - Enter new login
        - Enter new email
        - Enter new password
        - Click button
        - Verify registration is successful
        """

        username_reg = random_str()
        email_reg = f"{random_str()}{random_num()}@mail.com"
        password_reg = random_str(), random_num()

        start_page.sign_up(username_reg, email_reg, password_reg)
        self.log.info("Logged")

        start_page.verify_success_sign_up(username_reg)
        self.log.info("Verified")
