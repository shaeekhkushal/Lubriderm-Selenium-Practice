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

    def email_sign_up(self):
        try:
            emai_sign_up = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.email_sign_up)))
            emai_sign_up.click()
            time.sleep(2)
            title = self.driver.title
            current_url = self.driver.current_url
            print("Current Title is:", title)
            print("Current URL is:", current_url)
            self.driver.back()

        except TimeoutException:
            print("Email sign up element not found within the specified time.")
        time.sleep(2)
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
            print("Navigation Text:", click_on_all_products.text)
            time.sleep(1)
            click_on_all_products.click()
            time.sleep(2)
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
            print("Navigation Text:", click_on_daily_moisture.text)
            time.sleep(1)
            click_on_daily_moisture.click()
            time.sleep(2)
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

            click_on_advance_therapy = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.advance_therapy)))
            time.sleep(1)
            print("Navigation Text:", click_on_advance_therapy.text)
            time.sleep(1)
            click_on_advance_therapy.click()
            time.sleep(2)
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

            click_on_intense_skin_repair = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.intense_skin_repair)))
            time.sleep(1)
            print("Navigation Text:", click_on_intense_skin_repair.text)
            time.sleep(1)
            click_on_intense_skin_repair.click()
            time.sleep(2)
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

    def skin_concerns_nav(self):
        try:
            hover_on_skin_concerns = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.skin_concerns)))
            action = ActionChains(self.driver)
            print("hover_on_skin_concerns is:", hover_on_skin_concerns.text)
            action.move_to_element(hover_on_skin_concerns).perform()
            time.sleep(1)

            click_on_all_skin_concerns = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.all_skin_concerns)))
            time.sleep(1)
            print("Navigation Text:", click_on_all_skin_concerns.text)
            time.sleep(1)
            click_on_all_skin_concerns.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            hover_on_skin_concerns = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.skin_concerns)))
            action = ActionChains(self.driver)
            print("hover_on_skin_concerns is:", hover_on_skin_concerns.text)
            action.move_to_element(hover_on_skin_concerns).perform()
            time.sleep(1)

            click_on_normal_to_dry_skin = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.normal_to_dry_skin)))
            time.sleep(1)
            print("Navigation Text:", click_on_normal_to_dry_skin.text)
            time.sleep(1)
            click_on_normal_to_dry_skin.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            hover_on_skin_concerns = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.skin_concerns)))
            action = ActionChains(self.driver)
            print("hover_on_skin_concerns is:", hover_on_skin_concerns.text)
            action.move_to_element(hover_on_skin_concerns).perform()
            time.sleep(1)

            click_on_extra_dry_skin = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.extra_dry_skin)))
            time.sleep(1)
            print("Navigation Text:", click_on_extra_dry_skin.text)
            time.sleep(1)
            click_on_extra_dry_skin.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            hover_on_skin_concerns = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.skin_concerns)))
            action = ActionChains(self.driver)
            print("hover_on_skin_concerns is:", hover_on_skin_concerns.text)
            action.move_to_element(hover_on_skin_concerns).perform()
            time.sleep(1)

            click_on_mature_skin_care = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.mature_skin_care)))
            time.sleep(1)
            print("Navigation Text:", click_on_mature_skin_care.text)
            time.sleep(1)
            click_on_mature_skin_care.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            hover_on_skin_concerns = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.skin_concerns)))
            action = ActionChains(self.driver)
            print("hover_on_skin_concerns is:", hover_on_skin_concerns.text)
            action.move_to_element(hover_on_skin_concerns).perform()
            time.sleep(1)

            click_on_tattoo_after_care = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.tattoo_after_care)))
            time.sleep(1)
            print("Navigation Text:", click_on_tattoo_after_care.text)
            time.sleep(1)
            click_on_tattoo_after_care.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            hover_on_skin_concerns = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.skin_concerns)))
            action = ActionChains(self.driver)
            print("hover_on_skin_concerns is:", hover_on_skin_concerns.text)
            action.move_to_element(hover_on_skin_concerns).perform()
            time.sleep(1)

            click_on_itchy_dry_skin = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.itchy_dry_skin)))
            time.sleep(1)
            print("Navigation Text:", click_on_itchy_dry_skin.text)
            time.sleep(1)
            click_on_itchy_dry_skin.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            print("Skin Concerns element not found within the specified time.")
        time.sleep(2)
        return self

    def about_lubriderm(self):
        try:
            hover_on_about_lubriderm = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.about_lubriderm)))
            action = ActionChains(self.driver)
            print("hover_on_about_lubriderm is:", hover_on_about_lubriderm.text)
            action.move_to_element(hover_on_about_lubriderm).perform()
            time.sleep(1)

            click_on_overview = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.overview)))
            time.sleep(1)
            print("Navigation Text:", click_on_overview.text)
            time.sleep(1)
            click_on_overview.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            hover_on_about_lubriderm = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.about_lubriderm)))
            action = ActionChains(self.driver)
            print("hover_on_about_lubriderm is:", hover_on_about_lubriderm.text)
            action.move_to_element(hover_on_about_lubriderm).perform()
            time.sleep(1)

            click_on_our_ingredients = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.our_ingredients)))
            time.sleep(1)
            print("Navigation Text:", click_on_our_ingredients.text)
            time.sleep(1)
            click_on_our_ingredients.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            hover_on_about_lubriderm = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.about_lubriderm)))
            action = ActionChains(self.driver)
            print("hover_on_about_lubriderm is:", hover_on_about_lubriderm.text)
            action.move_to_element(hover_on_about_lubriderm).perform()
            time.sleep(1)

            click_on_contact_us = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.contact_us)))
            time.sleep(1)
            print("Navigation Text:", click_on_contact_us.text)
            time.sleep(1)
            click_on_contact_us.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            print("About Lubriderm element not found within the specified time.")
        time.sleep(2)
        return self

    def where_to_buy(self):
        try:
            where_to_buy = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HeaderLocators.where_to_buy)))
            where_to_buy.click()
            time.sleep(10)
            title = self.driver.title
            current_url = self.driver.current_url
            print("Current Title is:", title)
            print("Current URL is:", current_url)
            self.driver.back()

        except TimeoutException:
            print("Email sign up element not found within the specified time.")
        time.sleep(2)
        return self
    