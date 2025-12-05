from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    # locators
    from_field = (By.ID, "from")
    to_field = (By.ID, "to")
    call_taxi_button = (By.CLASS_NAME, "call-taxi")
    supportive_plan = (By.XPATH, "//div[contains(@class, 'tcard') and text()='Supportive']")
    phone_field = (By.ID, "phone")
    sms_code_field = (By.ID, "code")
    add_card_button = (By.CLASS_NAME, "add-card")
    card_number_field = (By.ID, "number")
    card_code_field = (By.ID, "code")
    link_button = (By.CLASS_NAME, "link")
    comment_field = (By.ID, "comment")
    blanket_checkbox = (By.ID, "blanket")
    ice_cream_button = (By.ID, "icecream")
    car_search_modal = (By.ID, "car-search")

    # methods
    def set_route(self, from_address, to_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from_value(self):
        return self.driver.find_element(*self.from_field).get_attribute("value")

    def get_to_value(self):
        return self.driver.find_element(*self.to_field).get_attribute("value")

    def click_call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()

    def select_supportive_plan(self):
        plan = self.driver.find_element(*self.supportive_plan)
        if "active" not in plan.get_attribute("class"):
            plan.click()
        self.driver.find_element(*self.phone_field).send_keys(phone)
        self.driver.find_element(*self.sms_code_field).send_keys(sms_code)

    def add_card(self, number, code):
        self.driver.find_element(*self.add_card_button).click()
        self.driver.find_element(*self.card_number_field).send_keys(number)
        code_field = self.driver.find_element(*self.card_code_field)
        code_field.send_keys(code)
        code_field.send_keys(Keys.TAB)
        self.driver.find_element(*self.link_button).click()

    def get_payment_method(self):
        return self.driver.find_element(*self.payment_method_label).text

    def add_comment_for_driver(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def order_blanket_and_handkerchiefs(self):
        checkbox = self.driver.find_element(*self.blanket_checkbox)
        checkbox.click()
        return checkbox.get_property("checked")

    def order_ice_creams(self, count=2):
        for i in range(count):
            self.driver.find_element(*self.ice_cream_button).click()
        return self.driver.find_element(By.ID, "icecream-count").text

    def car_search_modal_displayed(self):
        return self.driver.find_element(*self.car_search_modal).is_displayed()
