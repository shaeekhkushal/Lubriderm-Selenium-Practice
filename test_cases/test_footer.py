import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.footer_po import Footer


class TestFooter:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.Footer = Footer(self.driver)
        yield
        self.driver.quit()

    def test_back_to_top(self):
        self.Footer.load()
        self.Footer.back_to_top()

    def test_footer_form(self):
        self.Footer.load()
        self.Footer.footer_form()

    def test_footer_product_menu(self):
        self.Footer.load()
        self.Footer.footer_product_menu()

    def test_footer_company_info_menu(self):
        self.Footer.load()
        self.Footer.footer_company_info_menu()

    def test_footer_legal_menu(self):
        self.Footer.load()
        self.Footer.footer_legal_menu()
