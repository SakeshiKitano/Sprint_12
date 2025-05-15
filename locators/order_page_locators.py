from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    STATION_IN_DROPDOWN = (By.XPATH, ".//li[@class='select-search__row']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']")
    PER_ONE_DAY = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    PER_TWO_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    ORDERED_FORM_HEADER = (By.XPATH, "//div[@class = 'Order_ModalHeader__3FDaJ' and contains(., 'Заказ оформлен')]")
