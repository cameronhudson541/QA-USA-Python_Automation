import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Keys


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # locators
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    CALL_A_TAXI_BUTTON = (By.XPATH, "//button[text()='Call a taxi']")
    SUPPORTIVE_PLAN = (By.XPATH, "//div[text()='Supportive']")
    PHONE_NUMBER = (By.XPATH, "//div[text()='Phone number']")
    PHONE_NUMBER_BUTTON = (By.CSS_SELECTOR, "div.np-text")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@id='phone']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    CODE_FIELD = (By.XPATH, "//input[@id='code']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    CARD_NUMBER_FIELD = (By.XPATH, "//input[@id='number']")
    CARD_CODE_FIELD = (By.XPATH, "//input[@id='code' and @class='card-input']")
    CARD_LINK_ = (By.XPATH, "//button[text()='Link']")
    BLANKET_AND_HANDKERCHIEFS_CHECKBOX = (By.XPATH, "//input[@class='switch-input']")
    ICE_CREAM_OPTION = (By.XPATH, "//div[@class='counter-value']")
    ICE_CREAM_BUTTON = (By.XPATH, "//div[@class='counter-plus']")
    DRIVER_COMMENT_FIELD = (By.XPATH, "//input[@id='comment']")
    PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[@class='pp-value-text']")
    ADD_CARD_BUTTON = (By.CLASS_NAME, "pp-plus")
    CAR_SEARCH_MODAL = (By.XPATH, "//div[text()='Car search']")
    ACTIVE_PLAN_TITLE = (By.CSS_SELECTOR, ".tcard.active .tcard-title")
    BLANKET_AND_HANDKERCHIEFS_BUTTON = (By.CLASS_NAME, 'switch')
    ORDER_BUTTON = (By.CLASS_NAME, 'smart-button')

    def input_from_address(self, from_address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(from_address)

    def input_to_address(self, to_address):
        self.driver.find_element(*self.TO_FIELD).send_keys(to_address)

    def get_from_address(self):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute("value")

    def get_to_address(self):
        return self.driver.find_element(*self.TO_FIELD).get_attribute("value")

    def call_a_taxi_button(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(self.CALL_A_TAXI_BUTTON)).click()

    def select_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN).click()

    def is_supportive_selected(self):
        active_title = self.driver.find_element(*self.ACTIVE_PLAN_TITLE).text
        return "Supportive" == active_title

    def fill_phone_number(self):
        self.driver.find_element(*self.PHONE_NUMBER).click()

    def get_phone_number_displayed(self):
        return self.driver.find_element(*self.PHONE_NUMBER_BUTTON).text

    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).click()

    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD_BUTTON).click()

    def fill_card_number(self):
        self.driver.find_element(*self.CARD_NUMBER_FIELD).send_keys(data.CARD_NUMBER)

    def fill_card_code(self):
        self.driver.find_element(*self.CARD_CODE_FIELD).send_keys(data.CARD_CODE)
        self.driver.find_element(*self.CARD_CODE_FIELD).send_keys(Keys.TAB)

    def click_link(self):
        self.driver.find_element(*self.CARD_LINK_).click()

    def get_payment_method_displayed(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_BUTTON).text

    def write_phone_number(self, phone):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(phone)

    def click_next(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def write_code(self, code):
        self.driver.find_element(*self.CODE_FIELD).send_keys(code)

    def click_confirm(self):
        self.driver.find_element(*self.CONFIRM_BUTTON).click()

    def get_call_a_taxi_button(self):
        return self.driver.find_element(*self.CALL_A_TAXI_BUTTON).text

    def order_ice_creams(self, count):
        for _ in range(count):
         self.driver.find_element(*self.ICE_CREAM_BUTTON).click()

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def get_ice_cream(self):
        return self.driver.find_element(*self.ICE_CREAM_OPTION).text

    def click_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_BUTTON).click()

    def is_blanket_and_handkerchiefs_selected(self):
        checkbox = self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_CHECKBOX)
        return checkbox.is_selected()

    def fill_driver_comment(self):
        self.driver.find_element(*self.DRIVER_COMMENT_FIELD).send_keys(data.MESSAGE_FOR_DRIVER)

    def driver_comment_field(self):
        return self.driver.find_element(*self.DRIVER_COMMENT_FIELD).get_attribute("value")

    def test_car_search_model_appears(self):
        modal = self.driver.find_element(*self.CAR_SEARCH_MODAL)
        return modal.is_displayed()
