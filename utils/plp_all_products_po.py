import time
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from selectors.plp_all_products_selectors import PlpAllProducts


class Plp:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def load(self):
        self.driver.get(Config.plp_all_products)
        title = self.driver.title
        current_url = self.driver.current_url
        logging.info("Current Title is: %s", title)
        logging.info("Current URL is: %s", current_url)
        time.sleep(5)
        return self

    def close_pop_up(self):
        try:
            close_pop_up = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.bottom_pop_up_close)))
            time.sleep(1)
            close_pop_up.click()

        except TimeoutException:
            logging.info("close_pop_up element not found within the specified time. %s")
        time.sleep(2)
        return self

    def banner(self):
        try:
            grab_banner_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.banner_header)))
            logging.info("Header Text: %s", grab_banner_header_text.text)

            grab_banner_sub_copy_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.banner_sub_copy)))
            logging.info("Sub copy Text: %s", grab_banner_sub_copy_text.text)

            banner_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.banner_image)))

            if banner_image.is_displayed():
                alt_text = banner_image.get_attribute('alt')
                logging.info("Main image is present and the Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! Main image is not present !!!!!!!!!!")

        except TimeoutException:
            logging.info("banner element not found within the specified time. %s")
        time.sleep(2)
        return self

    def product_1(self):
        try:
            scroll_to_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_first_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_products_cards)
            time.sleep(1)

            product1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product1_image)))

            if product1.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            product1.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_first_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_products_cards)
            time.sleep(1)

            check_first_eye_brow_tag = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.first_eye_brow_tag)))

            logging.info("Eye Brow tag for first product is: %s", check_first_eye_brow_tag.text)

            click_on_product1_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product1_name)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_product1_name.text)
            time.sleep(1)
            click_on_product1_name.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_first_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_products_cards)
            time.sleep(1)

            click_on_first_buy_now_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product1_buy_now_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_first_buy_now_cta.text)
            time.sleep(1)
            click_on_first_buy_now_cta.click()
            time.sleep(5)

            price_spider_pop_up1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, PlpAllProducts.price_spider_pop_up1)))
            if price_spider_pop_up1.is_displayed():
                logging.info("Price spider Pop up displayed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not displayed !!!!!!!!!! %s")

            price_spider_pop_up1_close = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, PlpAllProducts.price_spider_pop_up1_close)))
            price_spider_pop_up1_close.click()

            if price_spider_pop_up1_close.is_enabled():
                logging.info("Price spider Pop up closed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not closed !!!!!!!!!! %s")
            time.sleep(2)

        except TimeoutException:
            logging.info("product_1 element not found within the specified time. %s")
        time.sleep(2)
        return self

    def product_2(self):
        try:
            scroll_to_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_first_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_products_cards)
            time.sleep(2)

            product2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product2_image)))

            if product2.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            product2.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_first_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_products_cards)
            time.sleep(1)

            check_second_eye_brow_tag = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.second_eye_brow_tag)))

            logging.info("Eye Brow tag for first product is: %s", check_second_eye_brow_tag.text)

            click_on_product2_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product2_name)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_product2_name.text)
            time.sleep(1)
            click_on_product2_name.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_first_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_products_cards)
            time.sleep(1)

            click_on_second_buy_now_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product2_buy_now_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_second_buy_now_cta.text)
            time.sleep(1)
            click_on_second_buy_now_cta.click()
            time.sleep(5)

            price_spider_pop_up2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, PlpAllProducts.price_spider_pop_up2)))
            if price_spider_pop_up2.is_displayed():
                logging.info("Price spider Pop up displayed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not displayed !!!!!!!!!! %s")

            price_spider_pop_up2_close = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, PlpAllProducts.price_spider_pop_up2_close)))
            price_spider_pop_up2_close.click()

            if price_spider_pop_up2_close.is_enabled():
                logging.info("Price spider Pop up closed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not closed !!!!!!!!!! %s")
            time.sleep(2)

        except TimeoutException:
            logging.info("product_2 element not found within the specified time. %s")
        time.sleep(2)
        return self

    def product_3(self):
        try:
            scroll_to_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_first_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_products_cards)
            time.sleep(2)

            product3 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product3_image)))

            if product3.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            product3.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_first_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_products_cards)
            time.sleep(1)

            check_third_eye_brow_tag = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.third_eye_brow_tag)))

            logging.info("Eye Brow tag for first product is: %s", check_third_eye_brow_tag.text)

            click_on_product3_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product3_name)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_product3_name.text)
            time.sleep(1)
            click_on_product3_name.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_first_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_products_cards)
            time.sleep(1)

            click_on_third_buy_now_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product3_buy_now_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_third_buy_now_cta.text)
            time.sleep(1)
            click_on_third_buy_now_cta.click()
            time.sleep(5)

            price_spider_pop_up3 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, PlpAllProducts.price_spider_pop_up3)))
            if price_spider_pop_up3.is_displayed():
                logging.info("Price spider Pop up displayed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not displayed !!!!!!!!!! %s")

            price_spider_pop_up3_close = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, PlpAllProducts.price_spider_pop_up3_close)))
            price_spider_pop_up3_close.click()

            if price_spider_pop_up3_close.is_enabled():
                logging.info("Price spider Pop up closed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not closed !!!!!!!!!! %s")
            time.sleep(2)

        except TimeoutException:
            logging.info("product_3 element not found within the specified time. %s")
        time.sleep(2)
        return self

    def product_4(self):
        try:
            scroll_to_second_row_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_second_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_second_row_products_cards)
            time.sleep(2)

            product4 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product4_image)))

            if product4.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            product4.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_second_row_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_second_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_second_row_products_cards)
            time.sleep(2)

            check_fourth_eye_brow_tag = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.fourth_eye_brow_tag)))

            logging.info("Eye Brow tag for first product is: %s", check_fourth_eye_brow_tag.text)

            click_on_product4_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product4_name)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_product4_name.text)
            time.sleep(1)
            click_on_product4_name.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_second_row_products_cards = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.products_card_second_row)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_second_row_products_cards)
            time.sleep(2)

            click_on_fourth_buy_now_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, PlpAllProducts.product3_buy_now_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_fourth_buy_now_cta.text)
            time.sleep(1)
            click_on_fourth_buy_now_cta.click()
            time.sleep(5)

            price_spider_pop_up4 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, PlpAllProducts.price_spider_pop_up4)))
            if price_spider_pop_up4.is_displayed():
                logging.info("Price spider Pop up displayed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not displayed !!!!!!!!!! %s")

            price_spider_pop_up4_close = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, PlpAllProducts.price_spider_pop_up4_close)))
            price_spider_pop_up4_close.click()

            if price_spider_pop_up4_close.is_enabled():
                logging.info("Price spider Pop up closed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not closed !!!!!!!!!! %s")
            time.sleep(2)

        except TimeoutException:
            logging.info("product_3 element not found within the specified time. %s")
        time.sleep(2)
        return self
