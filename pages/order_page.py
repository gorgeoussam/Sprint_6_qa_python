import allure

from pages.base_page import BasePage
from locators.order_page_locators import *
from data import *


class OrderPage(BasePage):

    @allure.step('click order from the header')
    def click_button_in_header(self):
        self.find_element(BUTTON_ORDER_IN_HEADER).click()

    @allure.step('click order from the page')
    def click_button_in_page(self):

        self.scroll_into_view_and_click(BUTTON_ORDER_IN_PAGE)



    @allure.step('filling in request')
    def get_order(self, name, surname, address, subway, phone, time, comment):
        self.find_element(FIELD_NAME).send_keys(name)
        self.find_element(FIELD_SURNAME).send_keys(surname)
        self.find_element(FIELD_ADDRESS).send_keys(address)
        self.find_element(FIELD_SUBWAY).send_keys(subway)
        self.find_element(LIST_SUBWAY).click()
        self.find_element(FIELD_PHONE).send_keys(phone)
        self.find_element(BUTTON_NEXT).click()

        self.find_element(FIELD_TIME).send_keys(time)
        self.find_element(CALENDAR).click()
        self.find_element(DROPDOWN_RENTS).click()
        self.find_element(TIME_RENTS).click()
        self.find_element(CHECKBOX_COLOR_BLACK).click()
        self.find_element(FIELD_COMMENT).send_keys(comment)
        self.find_element(BUTTON_ORDER).click()

        self.find_element(BUTTON_YES).click()

        self.wait_for_visibility(VIEW_STATUS)
        description = self.find_element(VIEW_STATUS).text
        assert description == MESSAGE_ORDER

    @allure.step('click the logo')
    def click_logo_scooter(self):
        self.find_element(LOGO_SCOOTER).click()
        self.wait_for_url_to_be(MAIN_PAGE_URL)
        assert str(MAIN_PAGE_URL) == self.get_current_url()

    @allure.step('click Yandex logo')
    def click_logo_yandex(self):
        self.find_element(LOGO_YANDEX).click()
        self.switch_to_last_window()
        self.wait_for_url_to_be(REDIRECT_PAGE_URL)
        assert str(REDIRECT_PAGE_URL) == self.get_current_url()