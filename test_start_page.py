import logging
import random
import string
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.randint(111111, 999999))

    @staticmethod
    def random_str(length=5):
        """Generate random string"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    def test_incorrect_login(self):
        driver = webdriver.Chrome("/Users/bogdan/PycharmProjects/MyTestProject/chromedriver")

        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open start page")

        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("User1")
        sleep(1)

        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("1111")
        sleep(1)

        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        driver.close()

    def test_empty_login(self):
        """
        - Create driver
        - Open page
        - Clear login
        - Clear password
        - Click button
        - Verify error
        """
        driver = webdriver.Chrome("/Users/bogdan/PycharmProjects/MyTestProject/chromedriver")

        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        self.log.info("Open start page")

        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.clear()
        sleep(1)

        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(1)

        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.is_displayed()
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        driver.close()

    def test_symbols_asc2(self):
        driver = webdriver.Chrome("/Users/bogdan/PycharmProjects/MyTestProject/chromedriver")

        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys("♣☺♂")
        sleep(1)

        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("♣☺♂123456789")
        sleep(1)

        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.is_displayed()
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"

        driver.close()

    def test_valid_login(self):
        driver = webdriver.Chrome("/Users/bogdan/PycharmProjects/MyTestProject/chromedriver")

        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        username = "testuser"
        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.send_keys(username)
        sleep(1)

        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.send_keys("qwe123456789")
        sleep(1)

        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        assert username.lower() in hello_message.text
        assert hello_message.text == f"Hello {username.lower()}, your feed is empty."

        driver.close()

    def test_valid_registration(self):
        driver = webdriver.Chrome("/Users/bogdan/PycharmProjects/MyTestProject/chromedriver")

        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

        username_reg = self.random_str()
        username_registration = driver.find_element(by=By.XPATH, value=".//input[@id='username-register']")
        username_registration.send_keys(username_reg)
        sleep(1)

        email_reg = f"{self.random_str()}{self.random_num()}@mail.com"
        email_registration = driver.find_element(by=By.XPATH, value=".//input[@id='email-register']")
        email_registration.send_keys(email_reg)
        sleep(1)

        password_reg = self.random_num()
        password_registration = driver.find_element(by=By.XPATH, value=".//input[@id='password-register']")
        password_registration.send_keys(self.random_str(7) + password_reg)
        sleep(1)

        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign up for OurApp']")
        button.click()
        sleep(1)

        hello_message = driver.find_element(by=By.XPATH, value=".//h2")
        assert username_reg.lower() in hello_message.text
        assert hello_message.text == f"Hello {username_reg.lower()}, your feed is empty."
