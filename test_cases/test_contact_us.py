import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.contact_us_po import ContactUs


class TestContactUs:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.ContactUs = ContactUs(self.driver)
        yield
        self.driver.quit()

    def test_banner_section(self):
        self.ContactUs.load()
        self.ContactUs.close_pop_up()
        self.ContactUs.banner_section()

    def test_faq_section(self):
        self.ContactUs.load()
        self.ContactUs.close_pop_up()
        self.ContactUs.faq_section()
