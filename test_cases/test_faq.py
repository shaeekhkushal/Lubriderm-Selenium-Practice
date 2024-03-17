import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.faq_po import Faq


class TestFaq:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.Faq = Faq(self.driver)
        yield
        self.driver.quit()

    def test_banner(self):
        self.Faq.load()
        self.Faq.close_pop_up()
        self.Faq.banner()

    def test_product_recommendation(self):
        self.Faq.load()
        self.Faq.close_pop_up()
        self.Faq.product_recommendation()

    def test_products_section(self):
        self.Faq.load()
        self.Faq.close_pop_up()
        self.Faq.products_section()
