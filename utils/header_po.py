import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from selectors.header_selectors import HeaderLocators


class Header:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def load(self):
        self.driver.get(Config.base_url)
        title = self.driver.title
        current_url = self.driver.current_url
        print("Current Title is:", title)
        print("Current URL is:", current_url)

        time.sleep(5)
        return self

    def click_logo(self):
        try:
            logo_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.logo)))
            logo_element.click()
            title = self.driver.title
            current_url = self.driver.current_url
            print("Current Title is:", title)
            print("Current URL is:", current_url)

        except TimeoutException:
            print("Logo element not found within the specified time.")
        time.sleep(2)
        return self
