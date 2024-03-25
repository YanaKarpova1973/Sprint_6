from selenium.webdriver.common.by import By
class MainPageLocators:

    QUESTION_LOCATOR = By.ID, 'accordion__heading-{}'
    ANSWER_LOCATOR = By.ID, 'accordion__panel-{}'
    ORDER_ON_PAGE = By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]//button[1]'
    ORDER_IN_THE_CORNER = By.CLASS_NAME, 'Button_Button__ra12g'
    ORDER_STATUS = By.CLASS_NAME, 'Header_Link__1TAG7'
    ORDER_TEXT_RESULT = By.CLASS_NAME, "Order_Header__BZXOb"
    SCOOTER_LOGO = By.XPATH, "//img[@alt='Scooter']"
    YANDEX_LOGO = By.XPATH, "//img[@alt='Yandex']"
    MAIN_PAGE_TEXT = By.CLASS_NAME, "Home_Header__iJKdX"
    DZEN = By.CLASS_NAME, "dzen-desktop__overflowBackground-3D"
    COOKIES_BUTTON = By.XPATH, "//button[@id='rcc-confirm-button']"
