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
        self.Homepage.banner()

    def test_our_products_section(self):
        self.Homepage.load()
        self.Homepage.our_products_section()

    def test_our_bestsellers_section(self):
        self.Homepage.load()
        self.Homepage.our_bestsellers_section()

    def test_skin_concerns_section(self):
        self.Homepage.load()
        self.Homepage.skin_concerns_section()

    def test_related_content_section(self):
        self.Homepage.load()
        self.Homepage.related_content_section()
