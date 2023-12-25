import time
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from selectors.footer_selectors import FooterLocators


class Footer:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def load(self):
        self.driver.get(Config.base_url)
        title = self.driver.title
        current_url = self.driver.current_url
        logging.info("Current Title is: %s", title)
        logging.info("Current URL is: %s", current_url)
        time.sleep(5)
        return self

    def back_to_top(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            click_on_back_to_top = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.back_to_top)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_back_to_top.text)
            time.sleep(1)
            click_on_back_to_top.click()
            time.sleep(2)

        except TimeoutException:
            logging.info("Footer back_to_top element not found within the specified time. %s")
        time.sleep(2)
        return self

    def footer_form(self):
        try:
            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            grab_footer_form_header = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_form_header)))
            logging.info("Header Text: %s", grab_footer_form_header.text)

            grab_footer_form_sub_copy_1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_form_sub_copy_1)))
            logging.info("Sub copy 1 Text: %s", grab_footer_form_sub_copy_1.text)

            grab_footer_form_sub_copy_2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_form_sub_copy_2)))
            logging.info("Sub copy 2 Text: %s", grab_footer_form_sub_copy_2.text)

            input_first_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.input_name)))
            input_first_name.send_keys("Shaeekh Khan")
            time.sleep(3)
            input_email = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.input_email)))
            input_email.send_keys("shaeek.test.sji@gmail.com")
            time.sleep(2)

            grab_disclaimer_copy = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.disclaimer_copy)))
            logging.info("Sub copy 2 Text: %s", grab_disclaimer_copy.text)

            click_privacy_policy = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.privacy_policy_link_text)))
            original_tab = self.driver.current_window_handle
            click_privacy_policy.click()
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            self.driver.switch_to.window(original_tab)

            click_financial_incentive = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.financial_incentive)))
            click_financial_incentive.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            self.driver.back()

            # click_submit_cta = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, FooterLocators.submit_btn)))
            # time.sleep(1)
            # logging.info("CTA:", click_submit_cta.text)
            # time.sleep(1)
            # click_submit_cta.click()
            # time.sleep(2)

            # confirm_submission = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, FooterLocators.confirm_submit)))
            # if confirm_submission.is_displayed():
            #     logging.info(confirm_submission.text)
            # else:
            #     logging.info("!!!!!!!!!! Submission failed !!!!!!!!!!")

        except TimeoutException:
            logging.info("footer_form element not found within the specified time. %s")
        time.sleep(2)
        return self

    def footer_product_menu(self):
        try:
            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            click_on_footer_all_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_all_products)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_footer_all_products.text)
            time.sleep(1)
            click_on_footer_all_products.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)
            click_on_footer_disco_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_disco_products)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_footer_disco_products.text)
            time.sleep(1)
            click_on_footer_disco_products.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)
            click_on_footer_wtb = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_wtb)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_footer_wtb.text)
            time.sleep(1)
            click_on_footer_wtb.click()
            time.sleep(5)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)
            click_on_footer_faq = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_faq)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_footer_faq.text)
            time.sleep(1)
            click_on_footer_faq.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

        except TimeoutException:
            logging.info("footer_product_menu element not found within the specified time. %s")
        time.sleep(2)
        return self

    def footer_company_info_menu(self):
        try:
            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            click_on_footer_about_us = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_about_us)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_footer_about_us.text)
            time.sleep(1)
            click_on_footer_about_us.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            click_on_our_ingredients = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_our_ingredients)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_our_ingredients.text)
            time.sleep(1)
            click_on_our_ingredients.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            click_on_contact_us = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_contact_us)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_contact_us.text)
            time.sleep(1)
            click_on_contact_us.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

        except TimeoutException:
            logging.info("footer_company_info_menu element not found within the specified time. %s")
        time.sleep(2)
        return self

    def footer_legal_menu(self):
        try:
            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            click_on_footer_privacy_policy = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_privacy_policy)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_footer_privacy_policy.text)
            time.sleep(1)
            click_on_footer_privacy_policy.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            click_on_footer_terms_of_use = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_terms_of_use)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_footer_terms_of_use.text)
            time.sleep(1)
            click_on_footer_terms_of_use.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            click_on_ad_choice = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_ad_choice)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_ad_choice.text)
            time.sleep(1)
            click_on_ad_choice.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            click_on_limit_the_use = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_limit_the_use)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_limit_the_use.text)
            time.sleep(1)
            click_on_limit_the_use.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            click_on_do_not_sell = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_do_not_sell)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_do_not_sell.text)
            time.sleep(1)
            click_on_do_not_sell.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            click_on_cookie_policy = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_cookie_policy)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_cookie_policy.text)
            time.sleep(1)
            click_on_cookie_policy.click()
            time.sleep(2)
            logging.info(self.driver.title)
            logging.info(self.driver.current_url)
            time.sleep(3)
            self.driver.back()

            scroll_to_footer = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_footer)
            time.sleep(1)

            click_on_customise_cookie = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.footer_customize_cookie)))
            time.sleep(1)
            logging.info("Footer Navigation Text: %s", click_on_customise_cookie.text)
            time.sleep(1)
            click_on_customise_cookie.click()
            time.sleep(5)

            cookie_pop_up = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.cookie_pop_up)))
            if cookie_pop_up.is_displayed():
                logging.info("Pop up displayed %s")
            else:
                logging.info("!!!!!!!!!! Pop up not displayed !!!!!!!!!! %s")

            cookie_pop_up_close = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, FooterLocators.cookie_pop_up_close)))
            cookie_pop_up_close.click()
            time.sleep(2)

        except TimeoutException:
            logging.info("footer_legal_menu element not found within the specified time. %s")
        time.sleep(2)
        return self
