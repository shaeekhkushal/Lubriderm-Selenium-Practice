import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.header_po import Header


class TestHeader:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.header = Header(self.driver)
        yield
        self.driver.quit()

    def test_email_sign_up(self):
        self.header.load()
        self.header.email_sign_up()

    def test_click_logo(self):
        self.header.load()
        self.header.click_logo()

    def test_products_nav(self):
        self.header.load()
        self.header.products_nav()

    def test_skin_concerns_nav(self):
        self.header.load()
        self.header.skin_concerns_nav()

    def test_about_lubriderm(self):
        self.header.load()
        self.header.about_lubriderm()

    def test_where_to_buy(self):
        self.header.load()
        self.header.where_to_buy()
