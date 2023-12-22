import time

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
        print("Current Title is:", title)
        print("Current URL is:", current_url)
        time.sleep(5)
        return self

    def banner(self):
        try:
            grab_banner_header_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_header_text)))
            print("Header Text:", grab_banner_header_text.text)

            grab_banner_sub_copy_text = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_sub_copy_text)))
            print("Sub copy Text:", grab_banner_sub_copy_text.text)

            banner_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_sub_copy_text)))

            if banner_image.is_displayed():
                print("Banner image is present")
            else:
                print("!!!!!!!!!! Banner image not present !!!!!!!!!!")

            click_on_banner_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.banner_cta)))
            time.sleep(1)
            print("Banner CTA Text:", click_on_banner_cta.text)
            time.sleep(1)
            click_on_banner_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            print("banner element not found within the specified time.")
        time.sleep(2)
        return self

    def our_products_section(self):
        try:
            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)
            print("Section title is:", scroll_to_our_products.text)

            click_on_see_all_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.see_all_products)))
            time.sleep(1)
            print("CTA Text:", click_on_see_all_products.text)
            time.sleep(1)
            click_on_see_all_products.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product1_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product1_image)))

            if click_on_product1_image.is_displayed():
                print("Product image is present")
            else:
                print("!!!!!!!!!! Product image not present !!!!!!!!!!")
            time.sleep(1)

            click_on_product1_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product1_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product1_cta)))
            time.sleep(1)
            print("CTA Text:", click_on_product1_cta.text)
            time.sleep(1)
            click_on_product1_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product2_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product2_image)))

            if click_on_product2_image.is_displayed():
                print("Product image is present")
            else:
                print("!!!!!!!!!! Product image not present !!!!!!!!!!")
            time.sleep(1)

            click_on_product2_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product2_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product2_cta)))
            time.sleep(1)
            print("CTA Text:", click_on_product2_cta.text)
            time.sleep(1)
            click_on_product2_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product3_image = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product3_image)))

            if click_on_product3_image.is_displayed():
                print("Product image is present")
            else:
                print("!!!!!!!!!! Product image not present !!!!!!!!!!")
            time.sleep(1)

            click_on_product3_image.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

            scroll_to_our_products = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.our_products_section)))
            self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_our_products)
            time.sleep(1)

            click_on_product3_cta = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, HomepageLocators.product3_cta)))
            time.sleep(1)
            print("CTA Text:", click_on_product3_cta.text)
            time.sleep(1)
            click_on_product3_cta.click()
            time.sleep(2)
            current_url = self.driver.current_url
            title = self.driver.title
            print("Redirected URL is:", current_url)
            print("Page Title:", title)
            self.driver.back()
            time.sleep(1)

        except TimeoutException:
            print("our_products_section element not found within the specified time.")
        time.sleep(2)
        return self
