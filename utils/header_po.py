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

    def products_nav(self):
        try:
            hover_on_products = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.products)))
            action = ActionChains(self.driver)
            print("hover_on_products is:", hover_on_products.text)
            action.move_to_element(hover_on_products).perform()
            time.sleep(1)

            click_on_all_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.all_products)))
            time.sleep(1)
            print("First Navigation Text:", click_on_all_products.text)
            time.sleep(1)
            action.click(click_on_all_products).perform()
            time.sleep(1)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            hover_on_products = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.products)))
            action = ActionChains(self.driver)
            print("hover_on_products is:", hover_on_products.text)
            action.move_to_element(hover_on_products).perform()
            time.sleep(1)

            click_on_daily_moisture = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.daily_moisture)))
            time.sleep(1)
            print("First Navigation Text:", click_on_daily_moisture.text)
            time.sleep(1)
            action.click(click_on_daily_moisture).perform()
            time.sleep(1)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            print("Products element not found within the specified time.")
        time.sleep(2)
        return self
