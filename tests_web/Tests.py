__author__ = 'Afina P'
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from tests_web.Pages import SignUpPage, SignInPage, AddToCartPage, SearchProductPage
from tests_web.Locators import Constants


class EnvironmentSetup(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=Constants.driver)
        self.driver.get(Constants.baseURL)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, timeout=30)
        self.action = webdriver.ActionChains(self.driver)
        self.SignUpPage = SignUpPage(self.driver)
        self.SignInPage = SignInPage(self.driver)
        self.AddToCartPage = AddToCartPage(self.driver)
        self.SearchProductPage = SearchProductPage(self.driver)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_signup_with_nohp(self):
        self.SignUpPage.click_signup_form()
        self.SignUpPage.input_nohp_or_email("085772610027")
        self.SignUpPage.click_signup_nohp_or_email("No. HP kamu sudah benar?",
                                                    "Masukkan Kode Rahasia yang diterima via SMS di:")

    def test_signup_with_email(self):
        self.SignUpPage.click_signup_form()
        self.SignUpPage.input_nohp_or_email("afinapd03@gmail.com")
        self.SignUpPage.click_signup_nohp_or_email("Email kamu sudah benar?",
                                                    "Masukkan Kode Rahasia yang diterima via email di:")

    def test_signin(self):
        self.SignInPage.click_signin_form()
        self.SignInPage.input_username("afnpd03@gmail.com")
        self.SignInPage.input_password("niazkilam93")
        self.SignInPage.click_signin_button()

    def test_search_product_without_signin(self):
        self.SearchProductPage.search_product("samsung a50")
        self.SearchProductPage.delete_search()

    def test_search_product_with_signin(self):
        self.SignInPage.login_user("afnpd03@gmail.com", "niazkilam93")
        self.SearchProductPage.search_product("samsung a50")
        self.SearchProductPage.delete_search()

    def test_add_to_cart_without_signin(self):
        self.SearchProductPage.search_product("Delive Extra Large Mouse Pad Big")
        self.AddToCartPage.select_product()
        self.AddToCartPage.checkout_product()
        self.SignInPage.assert_signin_form()

    def test_add_to_cart_with_signin(self):
        self.SignInPage.login_user("afnpd03@gmail.com", "niazkilam93")
        self.SearchProductPage.search_product("Delive Extra Large Mouse Pad Big")
        self.AddToCartPage.select_product()
        self.AddToCartPage.checkout_product()
        self.AddToCartPage.check_cart()

if __name__ == '__main__':
    unittest.main()



