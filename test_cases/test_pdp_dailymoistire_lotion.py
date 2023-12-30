import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.pdp_dailymoisture_lotion_po import PdpPage1


class TestPDP:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.Pdp = PdpPage1(self.driver)
        yield
        self.driver.quit()

    def test_image_carousel(self):
        self.Pdp.load()
        self.Pdp.close_pop_up()
        self.Pdp.product_image()
        self.Pdp.image_carousel()

    def test_products_description_section(self):
        self.Pdp.load()
        self.Pdp.close_pop_up()
        self.Pdp.products_description_section()

    def test_jump_to_link_menu(self):
        self.Pdp.load()
        self.Pdp.close_pop_up()
        self.Pdp.jump_to_link_menu()

    def test_ingredients_section(self):
        self.Pdp.load()
        self.Pdp.close_pop_up()
        self.Pdp.ingredients_section()

    def test_you_may_also_like(self):
        self.Pdp.load()
        self.Pdp.close_pop_up()
        self.Pdp.you_may_also_like()
