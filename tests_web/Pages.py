import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests_web.Locators import SignUpElements, SignInElements, SearchElements, AddToCartElements


class BasePage(object):
    def __init__(self, driver):
        self.driver=driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_present(self, by_locator):
        elements = self.driver.find_elements(*by_locator)
        assert len(elements) != 0


class SignUpPage(BasePage):
    def click_signup_form(self):
        self.assert_element_text(SignUpElements.SIGNUP_FORM, "Daftar")
        self.click(SignUpElements.SIGNUP_FORM)
        self.assert_element_text(SignUpElements.ASSERT_SIGNUP_FORM, "Daftar dulu, yuk")

    def input_nohp_or_email(self, noHporEmail):
        self.enter_text(SignUpElements.FIELD_NOHP_OR_EMAIL, noHporEmail)

    def click_signup_button(self):
        self.click(SignUpElements.SIGNUP_BUTTON)
        time.sleep(5)
        elements = self.driver.find_elements(*SignUpElements.ASSERT_WRONG_VALIDATION)
        if len(elements) == 0:
            pass
        else:
            print("Sign Up Failed")
            raise

    def click_signup_nohp_or_email(self, text1, text2):
        self.click(SignUpElements.SIGNUP_BUTTON)
        self.assert_element_text(SignUpElements.ASSERT_VERIFICATION, text1)
        self.click(SignUpElements.SEND_CODE_BUTTON)
        time.sleep(2)
        self.assert_element_text(SignUpElements.ASSERT_VERIFICATION, text2)



class SignInPage(BasePage):
    def click_signin_form(self):
        self.assert_element_text(SignInElements.SIGNIN_FORM, "Login")
        self.click(SignInElements.SIGNIN_FORM)
        self.SignInPage = SignInPage(self.driver)
        self.SignInPage.assert_signin_form()

    def assert_signin_form(self):
        self.assert_element_text(SignInElements.ASSERT_SIGNIN_FORM, "Silakan masuk ke dalam akun kamu")

    def input_username(self, username):
        self.enter_text(SignInElements.FIELD_USERNAME, username)

    def input_password(self, password):
        self.enter_text(SignInElements.FIELD_PASSWORD, password)

    def click_signin_button(self):
        self.click(SignInElements.SIGNIN_BUTTON)
        time.sleep(3)
        elements = self.driver.find_elements(*SignInElements.ASSERT_SIGNIN)
        if len(elements) != 0:
            pass
        else:
            print("Sign In Failed")
            raise

    def login_user(self, username, password):
        self.SignInPage = SignInPage(self.driver)
        self.SignInPage.click_signin_form()
        self.SignInPage.input_username(username)
        self.SignInPage.input_password(password)
        self.SignInPage.click_signin_button()

class SearchProductPage(BasePage):
    def search_product(self, product):
        self.enter_text(SearchElements.FIELD_SEARCH, product)
        time.sleep(3)
        self.click(SearchElements.SEARCH_BUTTON)
        self.assert_element_text(SearchElements.ASSERT_SEARCH, "“"+product+"”")

    def delete_search(self):
        self.click(SearchElements.DELETE_SEARCH)

class AddToCartPage(BasePage):
    def select_product(self):
        self.click(AddToCartElements.PRODUCT_1)
        self.assert_element_text(AddToCartElements.ADD_CART_BUTTON, " Masukkan Keranjang")

    def checkout_product(self):
        self.click(AddToCartElements.ADD_CART_BUTTON)

    def check_cart(self):
        self.assert_element_text(AddToCartElements.DIALOG_CART, "Keranjang Belanja")
        self.click(AddToCartElements.SEE_CART)
        time.sleep(3)
        self.assert_element_text(AddToCartElements.ASSERT_CART, "Keranjang belanja")


