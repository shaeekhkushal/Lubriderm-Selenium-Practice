import time
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from selectors.homepage_selectors import HomepageLocators


class Homepage:
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

    def banner(self):
        try:
            grab_banner_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_header_text)))
            logging.info("Header Text: %s", grab_banner_header_text.text)

            grab_banner_sub_copy_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_sub_copy_text)))
            logging.info("Sub copy Text: %s", grab_banner_sub_copy_text.text)

            banner_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_sub_copy_text)))

            if banner_image.is_displayed():
                logging.info("Banner image is present %s")
            else:
                logging.info("!!!!!!!!!! Banner image not present !!!!!!!!!! %s")

            click_on_banner_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_cta)))
            time.sleep(1)
            logging.info("Banner CTA Text: %s", click_on_banner_cta.text)
            time.sleep(1)
            click_on_banner_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            logging.info("banner element not found within the specified time. %s")
        time.sleep(2)
        return self

    def our_products_section(self):
        try:
            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_our_products.text)

            click_on_see_all_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.see_all_products)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_see_all_products.text)
            time.sleep(1)
            click_on_see_all_products.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product1_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product1_image)))

            if click_on_product1_image.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_product1_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product1_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product1_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_product1_cta.text)
            time.sleep(1)
            click_on_product1_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product2_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product2_image)))

            if click_on_product2_image.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_product2_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product2_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product2_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_product2_cta.text)
            time.sleep(1)
            click_on_product2_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product3_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product3_image)))

            if click_on_product3_image.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_product3_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product3_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product3_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_product3_cta.text)
            time.sleep(1)
            click_on_product3_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            logging.info("our_products_section element not found within the specified time. %s")
        time.sleep(2)
        return self

    def our_bestsellers_section(self):
        try:
            scroll_to_our_bestsellers = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_bestseller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_bestsellers)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_our_bestsellers.text)

            product_card1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product1_card_image)))

            if product_card1.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_product_card1_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product1_card_image)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_product_card1_image.text)
            time.sleep(1)
            click_on_product_card1_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_bestsellers = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_bestseller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_bestsellers)
            time.sleep(1)

            click_on_product_card1_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product1_card_name)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_product_card1_name.text)
            time.sleep(1)
            click_on_product_card1_name.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            # scroll_to_our_bestsellers = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, HomepageLocators.our_bestseller)))
            # self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_bestsellers)
            # time.sleep(1)
            #
            # click_on_buy_now_cta1 = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, HomepageLocators.buy_now1)))
            # time.sleep(1)
            # logging.info("CTA Text: %s", click_on_buy_now_cta1.text)
            # time.sleep(1)
            # click_on_buy_now_cta1.click()
            # time.sleep(5)
            #
            # price_spider_pop_up1 = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, HomepageLocators.price_spider_pop_up1)))
            # if price_spider_pop_up1.is_displayed():
            #     logging.info("Price spider Pop up displayed %s")
            # else:
            #     logging.info("!!!!!!!!!! Price spider Pop up not displayed !!!!!!!!!! %s")
            #
            # price_spider_pop_up1_close = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, HomepageLocators.price_spider_pop_up1_close)))
            # price_spider_pop_up1_close.click()
            #
            # if price_spider_pop_up1_close.is_enabled():
            #     logging.info("Price spider Pop up closed %s")
            # else:
            #     logging.info("!!!!!!!!!! Price spider Pop up not closed !!!!!!!!!! %s")
            # time.sleep(2)

            scroll_to_our_bestsellers = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_bestseller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_bestsellers)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_our_bestsellers.text)

            product_card2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product2_card_image)))

            if product_card2.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_product_card2_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product2_card_image)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_product_card2_image.text)
            time.sleep(1)
            click_on_product_card2_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_bestsellers = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_bestseller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_bestsellers)
            time.sleep(1)

            click_on_product_card2_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product2_card_name)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_product_card2_name.text)
            time.sleep(1)
            click_on_product_card2_name.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            # scroll_to_our_bestsellers = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, HomepageLocators.our_bestseller)))
            # self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_bestsellers)
            # time.sleep(1)
            #
            # click_on_buy_now_cta2 = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, HomepageLocators.buy_now2)))
            # time.sleep(1)
            # logging.info("CTA Text: %s", click_on_buy_now_cta2.text)
            # time.sleep(1)
            # click_on_buy_now_cta2.click()
            # time.sleep(5)
            #
            # price_spider_pop_up2 = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, HomepageLocators.price_spider_pop_up2)))
            # if price_spider_pop_up2.is_displayed():
            #     logging.info("Price spider Pop up displayed %s")
            # else:
            #     logging.info("!!!!!!!!!! Price spider Pop up not displayed !!!!!!!!!! %s")
            #
            # price_spider_pop_up2_close = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, HomepageLocators.price_spider_pop_up2_close)))
            # price_spider_pop_up2_close.click()
            #
            # if price_spider_pop_up2_close.is_enabled():
            #     logging.info("Price spider Pop up closed %s")
            # else:
            #     logging.info("!!!!!!!!!! Price spider Pop up not closed !!!!!!!!!! %s")
            # time.sleep(2)

            scroll_to_our_bestsellers = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_bestseller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_bestsellers)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_our_bestsellers.text)

            product_card3 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product3_card_image)))

            if product_card3.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_product_card3_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product3_card_image)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_product_card3_image.text)
            time.sleep(1)
            click_on_product_card3_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_bestsellers = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_bestseller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_bestsellers)
            time.sleep(1)

            click_on_product_card3_name = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product3_card_name)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_product_card3_name.text)
            time.sleep(1)
            click_on_product_card3_name.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            # scroll_to_our_bestsellers = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, HomepageLocators.our_bestseller)))
            # self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_bestsellers)
            # time.sleep(1)
            #
            # click_on_buy_now_cta3 = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, HomepageLocators.buy_now3)))
            # time.sleep(1)
            # logging.info("CTA Text: %s", click_on_buy_now_cta3.text)
            # time.sleep(1)
            # click_on_buy_now_cta3.click()
            # time.sleep(5)
            #
            # price_spider_pop_up3 = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, HomepageLocators.price_spider_pop_up3)))
            # if price_spider_pop_up3.is_displayed():
            #     logging.info("Price spider Pop up displayed %s")
            # else:
            #     logging.info("!!!!!!!!!! Price spider Pop up not displayed !!!!!!!!!! %s")
            #
            # price_spider_pop_up3_close = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((By.CLASS_NAME, HomepageLocators.price_spider_pop_up3_close)))
            # price_spider_pop_up3_close.click()
            #
            # if price_spider_pop_up3_close.is_enabled():
            #     logging.info("Price spider Pop up closed %s")
            # else:
            #     logging.info("!!!!!!!!!! Price spider Pop up not closed !!!!!!!!!! %s")
            # time.sleep(2)

        except TimeoutException:
            logging.info("our_bestsellers_section element not found within the specified time. %s")
        time.sleep(2)
        return self

    def skin_concerns_section(self):
        try:
            scroll_to_skin_concerns = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_skin_concerns)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_skin_concerns.text)

            click_on_all_skin_concerns = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.all_skin_concerns)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_all_skin_concerns.text)
            time.sleep(1)
            click_on_all_skin_concerns.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_skin_concerns = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_skin_concerns)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_skin_concerns.text)

            click_on_skin_concerns1_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns1_image)))

            if click_on_skin_concerns1_image.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_skin_concerns1_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_skin_concerns = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_skin_concerns)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_skin_concerns.text)

            click_on_skin_concerns1_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns1_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_skin_concerns1_cta.text)
            time.sleep(1)
            click_on_skin_concerns1_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_skin_concerns = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_skin_concerns)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_skin_concerns.text)

            click_on_skin_concerns2_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns2_image)))

            if click_on_skin_concerns2_image.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_skin_concerns2_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_skin_concerns = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_skin_concerns)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_skin_concerns.text)

            click_on_skin_concerns2_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns2_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_skin_concerns2_cta.text)
            time.sleep(1)
            click_on_skin_concerns2_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_skin_concerns = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_skin_concerns)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_skin_concerns.text)

            click_on_skin_concerns3_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns3_image)))

            if click_on_skin_concerns3_image.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_skin_concerns3_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_skin_concerns = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_skin_concerns)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_skin_concerns.text)

            click_on_skin_concerns3_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns3_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_skin_concerns3_cta.text)
            time.sleep(1)
            click_on_skin_concerns3_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_skin_concerns = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_skin_concerns)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_skin_concerns.text)

            click_on_skin_concerns4_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns4_image)))

            if click_on_skin_concerns4_image.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_skin_concerns4_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_skin_concerns = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_skin_concerns)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_skin_concerns.text)

            click_on_skin_concerns4_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.skin_concerns4_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_skin_concerns4_cta.text)
            time.sleep(1)
            click_on_skin_concerns4_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            logging.info("skin_concerns_section element not found within the specified time. %s")
        time.sleep(2)
        return self

    def related_content_section(self):
        try:
            scroll_to_related_content = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.related_content)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_related_content)
            time.sleep(1)
            logging.info("Section title is: %s", scroll_to_related_content.text)

            click_on_related_content1_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.related_content_image1)))

            if click_on_related_content1_image.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_related_content1_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_related_content = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.related_content)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_related_content)
            time.sleep(1)

            grab_related_content_header1_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.related_content_header1_text)))
            logging.info("Sub copy Text: %s", grab_related_content_header1_text.text)

            click_on_related_content1_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.related_content1_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_related_content1_cta.text)
            time.sleep(1)
            click_on_related_content1_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_related_content = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.related_content)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_related_content)
            time.sleep(1)

            click_on_related_content2_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.related_content_image2)))

            if click_on_related_content2_image.is_displayed():
                logging.info("Product image is present %s")
            else:
                logging.info("!!!!!!!!!! Product image not present !!!!!!!!!! %s")
            time.sleep(1)

            click_on_related_content2_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_related_content = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.related_content)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_related_content)
            time.sleep(1)

            grab_related_content_header2_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.related_content_header2_text)))
            logging.info("Sub copy Text: %s", grab_related_content_header2_text.text)

            click_on_related_content2_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.related_content2_cta)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_related_content2_cta.text)
            time.sleep(1)
            click_on_related_content2_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            logging.info("related_content_section element not found within the specified time. %s")
        time.sleep(2)
        return self
