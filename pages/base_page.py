from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator)
        )

    def scroll_into_view_and_click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def get_visible_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return element.text

    def wait_for_visibility(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def wait_for_clickability(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_url_to_be(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])