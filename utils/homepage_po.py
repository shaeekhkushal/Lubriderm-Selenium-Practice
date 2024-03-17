
import time
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Config
from selectors.homepage_selectors import HomepageLocators


def handle_exception(driver: object, error_message: object) -> object:
    logging.error(error_message)
    driver.close()
    assert False, error_message


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

    def close_pop_up(self):
        try:
            close_pop_up = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.close_bottom_pop_up)))
            time.sleep(1)
            close_pop_up.click()

        except TimeoutException:
            handle_exception(self.driver, "Pop-Up element not found within the specified time. %s")
        time.sleep(2)
        return self

    def banner_section(self):
        try:
            grab_banner_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_header_text)))
            logging.info(grab_banner_header_text.text)
            time.sleep(1)

            grab_banner_sub_copy_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_sub_copy_text)))
            logging.info(grab_banner_sub_copy_text.text)
            time.sleep(1)

            click_on_banner_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_cta)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_banner_cta.text)
            time.sleep(1)
            click_on_banner_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            banner_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_image_locators)))

            if banner_image.is_displayed():
                alt_text = banner_image.get_attribute('alt')
                logging.info("Main image is present and the Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! Main image is not present !!!!!!!!!!")

        except TimeoutException:
            handle_exception(self.driver, "Banner element not found within the specified time. %s")
        time.sleep(2)
        return self

    def shop_by_collection(self):
        try:
            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            grab_section_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.section_header_text)))
            logging.info(grab_section_header_text.text)
            time.sleep(1)

            click_on_see_all_product_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.see_all_product_cta)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_see_all_product_cta.text)
            time.sleep(1)
            click_on_see_all_product_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            daily_moisture_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.collection_image1)))

            if daily_moisture_image.is_displayed():
                alt_text = daily_moisture_image.get_attribute('alt')
                logging.info("Main image is present and the Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! Main image is not present !!!!!!!!!!")

            click_on_daily_moisture_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.collection_image1)))
            time.sleep(1)
            click_on_daily_moisture_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            daily_moisture_details_header = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.daily_moisture_details_header_text)))
            logging.info(daily_moisture_details_header.text)
            time.sleep(1)
            daily_moisture_details_header.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            grab_daily_moisture_details_sub_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.daily_moisture_details_sub_text)))
            logging.info(grab_daily_moisture_details_sub_text.text)
            time.sleep(1)

            click_on_daily_moisture_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.daily_moisture_cta)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_daily_moisture_cta.text)
            time.sleep(1)
            click_on_daily_moisture_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            advanced_therapy_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.collection_image2)))

            if advanced_therapy_image.is_displayed():
                alt_text = advanced_therapy_image.get_attribute('alt')
                logging.info("Main image is present and the Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! Main image is not present !!!!!!!!!!")

            click_on_advanced_therapy_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.collection_image2)))
            time.sleep(1)
            click_on_advanced_therapy_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            advanced_therapy_header = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.advanced_therapy_header_text)))
            logging.info(advanced_therapy_header.text)
            time.sleep(1)
            advanced_therapy_header.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            grab_advanced_therapy_sub_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.advanced_therapy_sub_text)))
            logging.info(grab_advanced_therapy_sub_text.text)
            time.sleep(1)

            click_on_advanced_therapy_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.advanced_therapy_cta)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_advanced_therapy_cta.text)
            time.sleep(1)
            click_on_advanced_therapy_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            intense_skin_repair_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.collection_image3)))

            if intense_skin_repair_image.is_displayed():
                alt_text = intense_skin_repair_image.get_attribute('alt')
                logging.info("Main image is present and the Alt text is: %s", alt_text)
            else:
                logging.info("!!!!!!!!!! Main image is not present !!!!!!!!!!")

            click_on_intense_skin_repair_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.collection_image3)))
            time.sleep(1)
            click_on_intense_skin_repair_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            intense_skin_repair_header = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.intense_skin_repair_header_text)))
            logging.info(intense_skin_repair_header.text)
            time.sleep(1)
            intense_skin_repair_header.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_shop_by_collection_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.shop_by_collection_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_shop_by_collection_section)
            time.sleep(3)

            grab_intense_skin_repair_sub_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.intense_skin_repair_sub_text)))
            logging.info(grab_intense_skin_repair_sub_text.text)
            time.sleep(1)

            click_on_intense_skin_repair_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.intense_skin_repair_cta)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_intense_skin_repair_cta.text)
            time.sleep(1)
            click_on_intense_skin_repair_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            handle_exception(self.driver, "Banner element not found within the specified time. %s")
        time.sleep(2)
        return self

    def about_lubriderm(self):
        try:
            scroll_to_video_section = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.video_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_video_section)
            time.sleep(3)

            about_lubriderm_video = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.video)))

            if about_lubriderm_video.is_displayed():
                logging.info("Video is present")
            else:
                logging.info("!!!!!!!!!! Video is not present !!!!!!!!!!")

            grab_about_lubriderm_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.about_lubriderm_header_text)))
            logging.info(grab_about_lubriderm_header_text.text)
            time.sleep(1)

            grab_about_lubriderm_sub_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.about_lubriderm_sub_text)))
            logging.info(grab_about_lubriderm_sub_text.text)
            time.sleep(1)

            click_on_about_us_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.about_us_cta)))
            time.sleep(1)
            logging.info("Product name Text: %s", click_on_about_us_cta.text)
            time.sleep(1)
            click_on_about_us_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            handle_exception(self.driver, "About Lubriderm element not found within the specified time. %s")
        time.sleep(2)
        return self

    def our_best_seller(self):
        try:
            scroll_to_our_best_seller = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_best_seller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_best_seller)
            time.sleep(1)

            grab_our_best_seller_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_best_seller_header_text)))
            logging.info("Section title is: %s", grab_our_best_seller_header_text.text)

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
            click_on_product_card1_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            logging.info("Redirected URL is: %s", current_url)
            logging.info("Page Title: %s", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_best_seller = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_best_seller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_best_seller)
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

            scroll_to_our_best_seller = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_best_seller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_best_seller)
            time.sleep(1)

            click_on_buy_now_cta1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.buy_now_cta1)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_buy_now_cta1.text)
            time.sleep(1)
            click_on_buy_now_cta1.click()
            time.sleep(10)

            price_spider_pop_up1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, HomepageLocators.price_spider_pop_up1)))
            if price_spider_pop_up1.is_displayed():
                logging.info("Price spider Pop up displayed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not displayed !!!!!!!!!! %s")

            price_spider_pop_up1_close = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, HomepageLocators.price_spider_pop_up1_close)))
            price_spider_pop_up1_close.click()

            if price_spider_pop_up1_close.is_enabled():
                logging.info("Price spider Pop up closed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not closed !!!!!!!!!! %s")
            time.sleep(2)

            scroll_to_our_best_seller = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_best_seller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_best_seller)
            time.sleep(1)

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

            scroll_to_our_best_seller = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_best_seller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_best_seller)
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

            scroll_to_our_best_seller = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_best_seller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_best_seller)
            time.sleep(1)

            click_on_buy_now_cta2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.buy_now_cta2)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_buy_now_cta2.text)
            time.sleep(1)
            click_on_buy_now_cta2.click()
            time.sleep(10)

            price_spider_pop_up2 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, HomepageLocators.price_spider_pop_up2)))
            if price_spider_pop_up2.is_displayed():
                logging.info("Price spider Pop up displayed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not displayed !!!!!!!!!! %s")

            price_spider_pop_up2_close = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, HomepageLocators.price_spider_pop_up2_close)))
            price_spider_pop_up2_close.click()

            if price_spider_pop_up2_close.is_enabled():
                logging.info("Price spider Pop up closed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not closed !!!!!!!!!! %s")
            time.sleep(2)

            scroll_to_our_best_seller = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_best_seller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_best_seller)
            time.sleep(1)

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

            scroll_to_our_best_seller = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_best_seller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_best_seller)
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

            scroll_to_our_best_seller = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_best_seller)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_best_seller)
            time.sleep(1)

            click_on_buy_now_cta3 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.buy_now_cta3)))
            time.sleep(1)
            logging.info("CTA Text: %s", click_on_buy_now_cta3.text)
            time.sleep(1)
            click_on_buy_now_cta3.click()
            time.sleep(10)

            price_spider_pop_up3 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, HomepageLocators.price_spider_pop_up3)))
            if price_spider_pop_up3.is_displayed():
                logging.info("Price spider Pop up displayed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not displayed !!!!!!!!!! %s")

            price_spider_pop_up3_close = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, HomepageLocators.price_spider_pop_up3_close)))
            price_spider_pop_up3_close.click()

            if price_spider_pop_up3_close.is_enabled():
                logging.info("Price spider Pop up closed %s")
            else:
                logging.info("!!!!!!!!!! Price spider Pop up not closed !!!!!!!!!! %s")
            time.sleep(2)

        except TimeoutException:
            handle_exception(self.driver, "Products element not found within the specified time. %s")
        time.sleep(2)
        return self
