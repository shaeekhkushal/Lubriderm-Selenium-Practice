import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.plp_all_products_po import Plp


class TestPLP:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.Plp = Plp(self.driver)
        yield
        self.driver.quit()

    def test_product_banner(self):
        self.Plp.load()
        self.Plp.close_pop_up()
        self.Plp.banner()

    def test_product_1(self):
        self.Plp.load()
        self.Plp.close_pop_up()
        self.Plp.product_1()

    def test_product_2(self):
        self.Plp.load()
        self.Plp.close_pop_up()
        self.Plp.product_2()

    def test_product_3(self):
        self.Plp.load()
        self.Plp.close_pop_up()
        self.Plp.product_3()

    def test_product_4(self):
        self.Plp.load()
        self.Plp.close_pop_up()
        self.Plp.product_4()

    def test_product_5(self):
        self.Plp.load()
        self.Plp.close_pop_up()
        self.Plp.product_5()

    def test_product_6(self):
        self.Plp.load()
        self.Plp.close_pop_up()
        self.Plp.product_6()

    def test_product_7(self):
        self.Plp.load()
        self.Plp.close_pop_up()
        self.Plp.product_7()

    def test_learn_more_about(self):
        self.Plp.load()
        self.Plp.close_pop_up()
        self.Plp.learn_more_about()
