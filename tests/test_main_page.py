import allure
import pytest
from selenium import webdriver

import data
from data import DESCRIPTIONS
from pages.main_page import MainPage


class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @pytest.mark.parametrize('accord_number, expected_answer', [
        (1, DESCRIPTIONS[1]),
        (2, DESCRIPTIONS[2]),
        (3, DESCRIPTIONS[3]),
        (4, DESCRIPTIONS[4]),
        (5, DESCRIPTIONS[5]),
        (6, DESCRIPTIONS[6]),
        (7, DESCRIPTIONS[7]),
        (8, DESCRIPTIONS[8])
    ])
    @allure.title('checking answers text {accord_number}')
    def test_check_accordions(self, accord_number, expected_answer):
        self.driver.get(data.MAIN_PAGE_URL)
        main_page = MainPage(self.driver)
        main_page.open_accordion(accord_number)
        actual_answer = main_page.get_answer_text(accord_number)
        assert actual_answer == expected_answer

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()