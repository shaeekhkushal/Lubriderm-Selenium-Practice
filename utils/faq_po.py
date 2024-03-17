import time
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from selectors.faq_selectors import FaqLocators


def handle_exception(driver: object, error_message: object) -> object:
    logging.error(error_message)
    driver.close()
    assert False, error_message


class Faq:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def load(self):
        self.driver.get(Config.faq)
        title = self.driver.title
        current_url = self.driver.current_url
        logging.info("Current Title is: %s", title)
        logging.info("Current URL is: %s", current_url)
        time.sleep(5)
        return self

    def close_pop_up(self):
        try:
            close_pop_up = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.bottom_pop_up_close)))
            time.sleep(1)
            close_pop_up.click()

        except TimeoutException:
            handle_exception(self.driver, "Products element not found within the specified time. %s")
        time.sleep(2)
        return self

    def banner(self):
        try:
            grab_banner_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.banner_header)))
            logging.info("Header Text: %s", grab_banner_header_text.text)

        except TimeoutException:
            handle_exception(self.driver, "Products element not found within the specified time. %s")
        time.sleep(2)
        return self

    def product_recommendation(self):
        try:
            grab_section_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.section_title1)))
            logging.info("Header Text: %s", grab_section_title.text)

            accordion1_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion1)))

            grab_accordion1_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion1_title)))
            logging.info("Header Text: %s", grab_accordion1_title.text)

            accordion1_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion1_plus_icon)))

            accordion1_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion1_minus_icon)))

            accordion1_scenarios.click()
            time.sleep(2)
            if accordion1_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion1_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion1_paragraph)))
            logging.info("Header Text: %s", grab_accordion1_paragraph.text)

            accordion1_scenarios.click()
            time.sleep(2)
            if accordion1_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            accordion2_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion2)))

            grab_accordion2_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion2_title)))
            logging.info("Header Text: %s", grab_accordion2_title.text)

            accordion2_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion2_plus_icon)))

            accordion2_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion2_minus_icon)))

            accordion2_scenarios.click()
            time.sleep(2)
            if accordion2_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion2_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion2_paragraph)))
            logging.info("Header Text: %s", grab_accordion2_paragraph.text)

            accordion2_scenarios.click()
            time.sleep(2)
            if accordion2_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            accordion3_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion3)))

            grab_accordion3_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion3_title)))
            logging.info("Header Text: %s", grab_accordion3_title.text)

            accordion3_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion3_plus_icon)))

            accordion3_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion3_minus_icon)))

            accordion3_scenarios.click()
            time.sleep(2)
            if accordion3_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion3_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion3_paragraph)))
            logging.info("Header Text: %s", grab_accordion3_paragraph.text)

            accordion3_scenarios.click()
            time.sleep(2)
            if accordion3_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

        except TimeoutException:
            handle_exception(self.driver, "Products element not found within the specified time. %s")
        time.sleep(2)
        return self

    def products_section(self):
        try:
            scroll_to_product_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.section_title2)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_product_section)

            grab_section_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.section_title2)))
            logging.info("Header Text: %s", grab_section_title.text)

            accordion4_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion4)))

            grab_accordion4_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion4_title)))
            logging.info("Header Text: %s", grab_accordion4_title.text)

            accordion4_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion4_plus_icon)))

            accordion4_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion4_minus_icon)))

            accordion4_scenarios.click()
            time.sleep(2)
            if accordion4_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion4_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion4_paragraph)))
            logging.info("Header Text: %s", grab_accordion4_paragraph.text)

            accordion4_scenarios.click()
            time.sleep(2)
            if accordion4_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            accordion5_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion5)))

            grab_accordion5_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion5_title)))
            logging.info("Header Text: %s", grab_accordion5_title.text)

            accordion5_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion5_plus_icon)))

            accordion5_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion5_minus_icon)))

            accordion5_scenarios.click()
            time.sleep(2)
            if accordion5_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion5_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion5_paragraph)))
            logging.info("Header Text: %s", grab_accordion5_paragraph.text)

            accordion5_scenarios.click()
            time.sleep(2)
            if accordion5_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            accordion6_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion6)))

            grab_accordion6_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion6_title)))
            logging.info("Header Text: %s", grab_accordion6_title.text)

            accordion6_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion6_plus_icon)))

            accordion6_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion6_minus_icon)))

            accordion6_scenarios.click()
            time.sleep(2)
            if accordion6_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion6_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion6_paragraph)))
            logging.info("Header Text: %s", grab_accordion6_paragraph.text)

            accordion6_scenarios.click()
            time.sleep(2)
            if accordion6_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            accordion7_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion7)))

            grab_accordion7_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion7_title)))
            logging.info("Header Text: %s", grab_accordion7_title.text)

            accordion7_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion7_plus_icon)))

            accordion7_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion7_minus_icon)))

            accordion7_scenarios.click()
            time.sleep(2)
            if accordion7_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion7_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion7_paragraph)))
            logging.info("Header Text: %s", grab_accordion7_paragraph.text)

            accordion7_scenarios.click()
            time.sleep(2)
            if accordion7_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            accordion8_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion8)))

            grab_accordion8_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion8_title)))
            logging.info("Header Text: %s", grab_accordion8_title.text)

            accordion8_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion8_plus_icon)))

            accordion8_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion8_minus_icon)))

            accordion8_scenarios.click()
            time.sleep(2)
            if accordion8_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion8_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion8_paragraph)))
            logging.info("Header Text: %s", grab_accordion8_paragraph.text)

            accordion8_scenarios.click()
            time.sleep(2)
            if accordion8_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            contact_us_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.accordion8_paragraph)))
            self.driver.execute_script("arguments[0].scrollIntoView();", contact_us_cta)

            grab_contact_us_section_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.contact_us_title)))
            logging.info("Header Text: %s", grab_contact_us_section_title.text)

            click_on_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FaqLocators.contact_us_cta)))
            logging.info("CTA Text: %s", click_on_cta.text)
            click_on_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            handle_exception(self.driver, "Products element not found within the specified time. %s")
        time.sleep(2)
        return self
