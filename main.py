import data
import helpers
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - logging enabled for phone confirmation retrieval
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("URBAN_ROUTES_URL reachable")
        else:
            print("URBAN_ROUTES_URL not reachable")

    def test_set_route(self):
        # Add in S8
        self.page.set_route(data.FROM_ADDRESS, data.TO_ADDRESS)
        assert self.page.driver.find_element(*self.page.from_field).get_attribute("value") == data.FROM_ADDRESS
        assert self.page.driver.find_element(*self.page.to_field).get_attribute("value") == data.TO_ADDRESS

    def test_select_plan(self):
        # Add in S8
        self.page.click_call_taxi()
        self.page.select_supportive_plan()
        plan = self.page.driver.find_element(*self.page.supportive_plan)
        assert "active" in plan.get_attribute("class")

    def test_fill_phone_number(self):
        # Add in S8
        sms_code = helpers.retrieve_phone_code(self.page.driver)
        self.page.fill_phone_number(data.PHONE_NUMBER, sms_code)
        assert self.page.driver.find_element(*self.page.phone_field).get_attribute("value") == data.PHONE_NUMBER

    def test_fill_card(self):
        # Add in S8
        self.page.add_card(data.CARD_NUMBER, data.CARD_CODE)
        payment_method = self.page.get_payment_method()
        assert payment_method == "Card"

    def test_comment_for_driver(self):
        # Add in S8
        self.page.add_comment_for_driver(data.DRIVER_COMMENT)
        assert self.page.driver.find_element(*self.page.comment_field).get_attribute("value") == data.DRIVER_COMMENT

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        assert self.page.order_blanket_and_handkerchiefs() is True

    def test_order_2_ice_creams(self):
        # Add in S8
        count = self.page.order_ice_creams(2)
        assert count == "2"

    def test_car_search_model_appears(self):
        # Add in S8
        self.page.add_comment_for_driver(data.DRIVER_COMMENT)
        assert self.page.car_search_modal_displayed() is True

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
