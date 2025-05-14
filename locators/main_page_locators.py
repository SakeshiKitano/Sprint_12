from selenium.webdriver.common.by import By


class MainPageLocators:
    TOP_BUTTON_ORDER = (By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[text()='Заказать']")
    MIDDLE_BUTTON_ORDER = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[text()='Заказать']")
    ACCORDION_BUTTON = (By.XPATH, "//div[@class='accordion__button' and text()='Я жизу за МКАДом, привезёте?']")
    QUESTION_LOCATOR = lambda question_text: (By.XPATH, f"//div[text()='{question_text}']")
    ANSWER_LOCATOR = lambda answer_text: (By.XPATH, f"//p[text()='{answer_text}']")
    APPLY_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    LOGO_SAMOKAT = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR" and @href="/"]')
    LOGO_YANDEX = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI" and @href="//yandex.ru"]')
    LOGO_DZEN = (By.XPATH, '//div[contains(@class, "logoContainer")]//a[@href="/" and contains(@class, "logoLink")]')