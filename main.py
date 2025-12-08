import data
import helpers
from selenium.webdriver import DesiredCapabilities
from pages import UrbanRoutesPage
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
        page.write_from_address(data.ADDRESS_FROM)
        page.write_to_address(data.ADDRESS_TO)
        assert page.get_from_address()==data.ADDRESS_FROM
        assert page.get_to_address() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.write_from_address(data.ADDRESS_FROM)
        page.write_to_address(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click.supportive()
        assert page.click_supportive() == True


    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.write_from_address(data.ADDRESS_FROM)
        page.write_to_address(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click.supportive()
        page.write_from_address(data.PHONE_NUMBER)
        page.click_next()
        page.write_code(helpers.retrieve_phone_code(self.driver))
        page.click_confirm()
        assert page.phone_number_field() == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.write_from_address(data.ADDRESS_FROM)
        page.write_to_address(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click.supportive()
        page.click_payment_method()
        page.click_add_card()
        page.fill_card_number()
        page.fill_card_code()
        page.click_link()
        assert page.card_number_field() == data.CARD_NUMBER


    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.write_from_address(data.ADDRESS_FROM)
        page.write_to_address(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click.supportive()
        page.fill_driver_comment()
        assert page.driver_comment_field() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self, checkbox):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.write_from_address(data.ADDRESS_FROM)
        page.write_to_address(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click.supportive()
        page.click_blanket_and_handkerchifs()
        assert checkbox.get_property("checked") is True

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)

        page.write_from_address(data.ADDRESS_FROM)
        page.write_to_address(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click_supportive()

        for _ in range(2):
            page.order_ice_creams()

        count = page.get_ice_cream_count()
        assert count == 2, f"Expected 2 ice creams but got {count}"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page = UrbanRoutesPage(self.driver)
        page.write_from_address(data.ADDRESS_FROM)
        page.write_to_address(data.ADDRESS_TO)
        page.click_call_taxi_button()
        page.click.supportive()
        page.write_from_address(data.PHONE_NUMBER)
        page.click_next()
        page.write_code(helpers.retrieve_phone_code(self.driver))
        page.click_confirm()
        page.fill_driver_message()
        page.click_order_button()
        assert page.is_car_modal_displayed() == True


    @classmethod
    def teardown_class(cls):
     cls.driver.quit()
