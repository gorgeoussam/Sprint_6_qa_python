from selenium.webdriver.common.by import By

LOGO_SCOOTER = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
LOGO_YANDEX = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

BUTTON_ORDER_IN_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')
BUTTON_ORDER_IN_PAGE = (By.CSS_SELECTOR, 'button.Button_Button__ra12g.Button_Middle__1CSJM')
FIELD_NAME = (By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder=\"* Имя\"]")
FIELD_SURNAME = (By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder=\"* Фамилия\"]")
FIELD_ADDRESS = (
    By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder=\"* Адрес: куда привезти заказ\"]")
FIELD_SUBWAY = (By.CSS_SELECTOR, "input.select-search__input[placeholder=\"* Станция метро\"]")
LIST_SUBWAY = (By.CLASS_NAME, 'select-search__select')
FIELD_PHONE = (By.CSS_SELECTOR,
               "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder=\"* Телефон: на него позвонит курьер\"]")
BUTTON_NEXT = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")
FIELD_TIME = (
    By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder=\"* Когда привезти самокат\"]")
CALENDAR = (By.CLASS_NAME, "react-datepicker__day--030")
DROPDOWN_RENTS = (By.CSS_SELECTOR, "div.Dropdown-control[aria-haspopup=\"listbox\"] .Dropdown-placeholder")
TIME_RENTS = (
    By.XPATH, "//div[@class='Dropdown-option' and @role='option' and @aria-selected='false' and text()='трое суток']")

CHECKBOX_COLOR_BLACK = (By.XPATH, '//*[@id="black"]')
CHECKBOX_COLOR_GRAY = (By.XPATH, '//*[@id="grey"]')
FIELD_COMMENT = (
    By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder=\"Комментарий для курьера\"]")
BUTTON_ORDER = (By.XPATH,
                "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and contains(text(), 'Заказать')]")

BUTTON_YES = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
VIEW_STATUS = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")