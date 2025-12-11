import data
import helpers
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage
import time

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("URBAN_ROUTES_URL reachable")

        else:
            print("URBAN_ROUTES_URL not reachable")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page =UrbanRoutesPage(self.driver)
        page.input_from_address(data.ADDRESS_FROM)
        page.input_to_address(data.ADDRESS_TO)
        assert page.get_from_address()==data.ADDRESS_FROM
        assert page.get_to_address() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.input_from_address(data.ADDRESS_FROM)
        page.input_to_address(data.ADDRESS_TO)
        page.call_a_taxi_button()
        page.select_supportive_plan()
        assert page.is_supportive_selected() == True


    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.input_from_address(data.ADDRESS_FROM)
        page.input_to_address(data.ADDRESS_TO)
        page.call_a_taxi_button()
        page.fill_phone_number()
        page.write_phone_number(data.PHONE_NUMBER)
        page.click_next()
        page.write_code(helpers.retrieve_phone_code(self.driver))
        page.click_confirm()
        assert page.get_phone_number_displayed() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.input_from_address(data.ADDRESS_FROM)
        page.input_to_address(data.ADDRESS_TO)
        page.call_a_taxi_button()
        page.select_supportive_plan()
        page.click_payment_method()
        time.sleep(2)
        page.click_add_card()
        page.fill_card_number()
        page.fill_card_code()
        page.click_link()
        assert page.get_payment_method_displayed() == 'Card'

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.input_from_address(data.ADDRESS_FROM)
        page.input_to_address(data.ADDRESS_TO)
        page.call_a_taxi_button()
        page.select_supportive_plan()
        page.fill_driver_comment()
        assert page.driver_comment_field() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.input_from_address(data.ADDRESS_FROM)
        page.input_to_address(data.ADDRESS_TO)
        page.call_a_taxi_button()
        page.select_supportive_plan()
        page.click_blanket_and_handkerchiefs()
        assert page.is_blanket_and_handkerchiefs_selected() == True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.input_from_address(data.ADDRESS_FROM)
        page.input_to_address(data.ADDRESS_TO)
        page.call_a_taxi_button()
        page.select_supportive_plan()
        page.order_ice_creams(2)
        count = int(page.get_ice_cream())
        assert count == 2, f"Expected 2 ice creams but got {count}"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page = UrbanRoutesPage(self.driver)
        page.input_from_address(data.ADDRESS_FROM)
        page.input_to_address(data.ADDRESS_TO)
        page.call_a_taxi_button()
        page.select_supportive_plan()
        page.fill_driver_comment()
        page.click_order_button()
        assert page.test_car_search_model_appears() == True


    @classmethod
    def teardown_class(cls):
     cls.driver.quit()
