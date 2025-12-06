from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    #locators
    FROM_FIELD=(By.ID, "from")
    TO_FIELD= (By.ID, "to")
    CALL_A_TAXI_BUTTON=(By.XPATH, "//button[text()='Call a taxi']")
    SUPPORTIVE_PLAN= (By.XPATH, "//div[text()='Supportive']")
    PHONE_NUMBER=(By.XPATH,"//div[text()='Phone number']")
    PHONE_NUMBER_FIELD=(By.XPATH,"//input[@id='phone']")
    NEXT_BUTTON=(By.XPATH, "//button[text()='Next']")
    CODE_FIELD=(By.XPATH, "//input[@id='code']")
    CONFIRM_BUTTON=(By.XPATH, "//button[text()='Confirm']")
    CARD_NUMBER_FIELD= (By.XPATH, "//input[@id='cardNumber']")
    CARD_CODE_FIELD=(By.XPATH, "//input[@id='cardCode']")
    CARD_LINK_=(By.XPATH, "//input[@id='cardLink']")
    BLANKET_AND_HANDKERCHIEFS_CHECKBOX=(By.XPATH, "//div[text()='Blankets and Hankerchiefs']")
    ICE_CREAM_OPTION = (By.XPATH, "//div[text()='Ice cream']")
    DRIVER_COMMENT=(By.XPATH, "//div[text()='Driver comment']")



    def input_from_address(self, from_address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(from_address)

    def input_to_address(self, to_address):
        self.driver.find_element(*self.TO_FIELD).send_keys(to_address)

    def get_from_address(self, from_address):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute("value")

    def get_to_address(self, to_address):
      return self.driver.find_element(*self.TO_FIELD).get_attribute("value")

    def call_a_taxi_button(self):
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON).click()

    def select_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN).click()

    def fill_phone_number(self):
        self.driver.find_element(*self.PHONE_NUMBER).click()

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

    def get_from_address(self, from_address):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute("value")

    def get_to_address(self, to_address):
        return self.driver.find_element(*self.TO_FIELD).get_attribute("value")

    def get_ice_cream(self):
        return self.driver.find_element(*self.ICE_CREAM_OPTION).text

    def get_driver_comment(self):
        return self.driver.find_element(*self.DRIVER_COMMENT).text

    def test_car_search_model_appears(self):
        modal = self.driver.find_element(*self.car_search_modal)
        return modal.is_displayed()
