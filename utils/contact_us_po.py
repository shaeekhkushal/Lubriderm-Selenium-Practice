import time
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from selectors.contact_us_selectors import ContactusLocators


def handle_exception(driver: object, error_message: object) -> object:
    logging.error(error_message)
    driver.close()
    assert False, error_message


class ContactUs:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def load(self):
        self.driver.get(Config.contact_us)
        title = self.driver.title
        current_url = self.driver.current_url
        logging.info("Current Title is: %s", title)
        logging.info("Current URL is: %s", current_url)
        time.sleep(5)
        return self

    def close_pop_up(self):
        try:
            close_pop_up = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.bottom_pop_up_close)))
            time.sleep(1)
            close_pop_up.click()

        except TimeoutException:
            handle_exception(self.driver, "Products element not found within the specified time. %s")
        time.sleep(2)
        return self

    def banner_section(self):
        try:
            grab_banner_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.banner_header)))
            logging.info("Header Text: %s", grab_banner_header_text.text)

        except TimeoutException:
            handle_exception(self.driver, "Products element not found within the specified time. %s")
        time.sleep(2)
        return self

    def faq_section(self):
        try:
            scroll_to_faq_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.section_title)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_faq_section)
            time.sleep(1)

            grab_section_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.section_title)))
            logging.info("Header Text: %s", grab_section_title.text)

            accordion1_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion1)))

            grab_accordion1_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion1_title)))
            logging.info("Header Text: %s", grab_accordion1_title.text)

            accordion1_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion1_plus_icon)))

            accordion1_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion1_minus_icon)))

            accordion1_scenarios.click()
            time.sleep(2)
            if accordion1_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion1_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion1_paragraph)))
            logging.info("Header Text: %s", grab_accordion1_paragraph.text)

            accordion1_scenarios.click()
            time.sleep(2)
            if accordion1_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            accordion2_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion2)))

            grab_accordion2_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion2_title)))
            logging.info("Header Text: %s", grab_accordion2_title.text)

            accordion2_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion2_plus_icon)))

            accordion2_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion2_minus_icon)))

            accordion2_scenarios.click()
            time.sleep(2)
            if accordion2_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion2_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion2_paragraph)))
            logging.info("Header Text: %s", grab_accordion2_paragraph.text)

            accordion2_scenarios.click()
            time.sleep(2)
            if accordion2_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            accordion3_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion3)))

            grab_accordion3_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion3_title)))
            logging.info("Header Text: %s", grab_accordion3_title.text)

            accordion3_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion3_plus_icon)))

            accordion3_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion3_minus_icon)))

            accordion3_scenarios.click()
            time.sleep(2)
            if accordion3_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion3_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion3_paragraph)))
            logging.info("Header Text: %s", grab_accordion3_paragraph.text)

            accordion3_scenarios.click()
            time.sleep(2)
            if accordion3_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            accordion4_scenarios = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion4)))

            grab_accordion4_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion4_title)))
            logging.info("Header Text: %s", grab_accordion4_title.text)

            accordion4_plus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion4_plus_icon)))

            accordion4_minus_icon = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion4_minus_icon)))

            accordion4_scenarios.click()
            time.sleep(2)
            if accordion4_minus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            grab_accordion4_paragraph = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.accordion4_paragraph)))
            logging.info("Header Text: %s", grab_accordion4_paragraph.text)

            accordion4_scenarios.click()
            time.sleep(2)
            if accordion4_plus_icon.is_displayed():
                logging.info("Scenario Passed")
            else:
                logging.info("!!!!! Scenario failed !!!!!")

            question_subcopy = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.sub_copy)))
            logging.info("Sub copy Text: %s", question_subcopy.text)

            click_on_all_faq_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, ContactusLocators.all_faq_cta)))
            logging.info("CTA Text: %s", click_on_all_faq_cta.text)
            click_on_all_faq_cta.click()
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
