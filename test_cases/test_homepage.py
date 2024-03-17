import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.homepage_po import Homepage


class TestHomepage:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.Homepage = Homepage(self.driver)
        yield
        self.driver.quit()

    def test_banner(self):
        self.Homepage.load()
        self.Homepage.close_pop_up()
        self.Homepage.banner_section()

    def test_shop_by_collection(self):
        self.Homepage.load()
        self.Homepage.close_pop_up()
        self.Homepage.shop_by_collection()

    def test_about_lubriderm(self):
        self.Homepage.load()
        self.Homepage.close_pop_up()
        self.Homepage.about_lubriderm()

    def test_our_best_seller(self):
        self.Homepage.load()
        self.Homepage.close_pop_up()
        self.Homepage.our_best_seller()

    def test_related_content_section(self):
        self.Homepage.load()
        self.Homepage.close_pop_up()
        self.Homepage.related_content_section()
