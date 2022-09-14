from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    def test_incorrect_login(self):
        driver = webdriver.Chrome("/Users/bogdan/PycharmProjects/MyTestProject/chromedriver")

        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")

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

        login = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login.clear()
        sleep(1)

        password = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password.clear()
        sleep(1)

        button = driver.find_element(by=By.XPATH, value=".//button[text()='Sign In']")
        button.click()
        sleep(1)

        driver.close()

        error_element = driver.find_element(by=By.XPATH, value=".//div[@class='alert alert-danger text-center']")
        assert error_element.is_displayed()
        assert error_element.text == "Invalid username / pasword", f"Actual message: {error_element.text}"
