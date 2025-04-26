import allure
import pytest
from selenium import webdriver

import data
from locators.order_page_locators import *
from pages.order_page import OrderPage


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize (
        'name, surname, address, metro_station, phone, time, comment', [
        ['Имя', 'Фамилия', 'Адрес', 'Комсомольская', '89011111111', '01.03.2025', 'коммент'],
        ['ИмяИмя', 'ФамилияФамилия', 'АдресАдрес', 'Комсомольская', '89011111111', '01.03.2025', 'коммент2']
        ]
    )
    @allure.title('order through header')
    def test_order_through_header(self, name, surname, address, metro_station, phone, time, comment):
        self.driver.get(data.MAIN_PAGE_URL)
        order_page = OrderPage(self.driver)
        order_page.click_button_in_header()
        order_page.get_order(name, surname, address, metro_station, phone, time, comment)

    @pytest.mark.parametrize (
        'name, surname, address, metro_station, phone, time, comment', [
        ['Имя', 'Фамилия', 'Адрес', 'Комсомольская', '89011111111', '01.03.2025', 'коммент'],
        ['ИмяИмя', 'ФамилияФамилия', 'АдресАдрес', 'Комсомольская', '89011111111', '01.03.2025', 'коммент2']
        ])
    @allure.title('order through page button')
    def test_order_button(self, name, surname, address, metro_station, phone, time, comment):
        self.driver.get(data.MAIN_PAGE_URL)
        order_page = OrderPage(self.driver)
        order_page.click_button_in_page()
        order_page.get_order(name, surname, address, metro_station, phone, time, comment)

    def test_scooter_redirect(self):
        self.driver.get(data.MAIN_PAGE_URL)
        order_page = OrderPage(self.driver)
        order_page.click_logo_scooter()

    def test_yandex_redirect(self):
        self.driver.get(data.MAIN_PAGE_URL)
        order_page = OrderPage(self.driver)
        order_page.click_logo_yandex()
