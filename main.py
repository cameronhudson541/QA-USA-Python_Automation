import data
import helpers
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

        # URL reachability check moved inside setup_class
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("URBAN_ROUTES_URL reachable")
        else:
            print("URBAN_ROUTES_URL not reachable")

    def test_set_route(self):
        # Add in S8
        print("function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for ordering blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        for i in range(2):
            # Add in S8
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car search model appears")
        pass

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
