from pages.Homepage import HomePage
from tests.Basetest import BaseTest


class TestSearch(BaseTest):
    def test_enter_valid_item(self):
        home_page=HomePage(self.driver)
        search_page=home_page.search_for_a_valid_product("HP")
        assert search_page.search_for_valid_product()


    def test_enter_invalid_item(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_valid_product("Honda")
        expected_text="There is no product that matches the search criteria."
        assert search_page.search_for_product()


    def test_enter_empty_item(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_valid_product("")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.search_for_product()