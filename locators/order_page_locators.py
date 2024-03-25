from selenium.webdriver.common.by import By
class OrderPageLocators:

    ORDER_BUTTON = By.CLASS_NAME, 'Button_Button__ra12g'
    FIRST_NAME = By.XPATH, "//input[@placeholder='* Имя']"
    LAST_NAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO = By.XPATH, "//input[@placeholder='* Станция метро']"
    CHOSEN_STATION = By.XPATH, "//div[text() = 'Комсомольская']"
    PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    ORDER_NEXT = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    DATE_CHOICE = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    DATE_CHOSEN = By.XPATH, "//div[text()='30']"
    RENT_PERIOD = By.CLASS_NAME, "Dropdown-control"
    TWO_DAYS = By.XPATH, "//div[text() = 'двое суток']"
    COMMENT = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    BLACK_PERL = By.ID, "black"
    MAKE_ORDER = By.XPATH, "//button[contains(@class,'Button_Button__ra12g Button_Middle__1CSJM')]/following-sibling::button[1]"
    ORDER_YES = By.XPATH, "//button[text()='Да']"
    ORDER_FORMED = By.CLASS_NAME, "Order_ModalHeader__3FDaJ"
    ORDER_WINDOW = By.CLASS_NAME, "Order_Text__2broi"
    CHECK_STATUS = By.XPATH, "//div[text() = 'Посмотреть статус']"
    ORDER_PAGE = By.CLASS_NAME, "Input_Input__1iN_Z Track_Input__1g7lq Input_Filled__1rDxs Input_Responsible__1jDKN"
