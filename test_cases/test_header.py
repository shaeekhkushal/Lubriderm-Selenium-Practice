import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.header_po import Header


class TestHeader(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.home_page = Header(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_click_logo(self):
        self.home_page.load()
        self.home_page.click_logo()

    def test_products_nav(self):
        self.home_page.load()
        self.home_page.products_nav()


if __name__ == "__main__":
    unittest.main()
