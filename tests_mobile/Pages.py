import time
from tests_mobile.Locators import SignInElements, SignUpElements


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def assert_element_text(self, by_locator, text):
        element = self.driver.find_element(*by_locator)
        assert element.text == text

    def enter_text(self, by_locator, text):
        element = self.driver.find_element(*by_locator)
        element.click()
        element.send_keys(text)

    def is_present(self, by_locator):
        elements = self.driver.find_elements(*by_locator)
        assert len(elements) != 0

class SignInPage(BasePage):
    def input_email(self, email):
        self.enter_text(SignInElements.FIELD_EMAIL, email)
        self.driver.back()

    def input_password(self, password):
        self.enter_text(SignInElements.FIELD_PASSWORD, password)
        self.driver.back()

    def click_signin_button(self):
        self.click(SignInElements.SIGNIN_BUTTON)

    def assert_signin_failed(self):
        self.assert_element_text(SignInElements.ASSERT_SNACKBAR, "Wrong Email or Password")

    def assert_signin_success(self):
        time.sleep(2)
        self.assert_element_text(SignInElements.ASSERT_SIGNIN_SUCCESS, "Android NewLine Learning")

    def user_signin(self, email, password):
        self.SignInPage = SignInPage(self.driver)
        self.SignInPage.input_email(email)
        self.SignInPage.input_password(password)
        self.SignInPage.click_signin_button()
        self.SignInPage.assert_signin_success()

    def click_signup_menu(self):
        self.click(SignInElements.SIGNUP_MENU)
        self.is_present(SignUpElements.SIGNUP_BUTTON)

class SignUpPage(BasePage):
    def click_signin_menu(self):
        self.click(SignUpElements.SIGNIN_MENU)
        self.is_present(SignInElements.SIGNIN_BUTTON)

    def input_name(self, name):
        self.enter_text(SignUpElements.FIELD_NAME, name)
        self.driver.back()

    def input_email(self, email):
        self.enter_text(SignUpElements.FIELD_EMAIL, email)
        self.driver.back()

    def input_password_and_confirm_password(self, password, confirmPassword):
        self.enter_text(SignUpElements.FIELD_PASSWORD, password)
        self.driver.back()
        self.enter_text(SignUpElements.FIELD_CONFIRM_PASSWORD, confirmPassword)
        self.driver.back()

    def click_signup_button(self):
        self.click(SignUpElements.SIGNUP_BUTTON)

    def assert_signup(self, text):
        print(self.driver.find_element(*SignUpElements.ASSERT_SNACKBAR))
        self.assert_element_text(SignUpElements.ASSERT_SNACKBAR, text)

    def user_signup(self, name, email, password, confirmPassword, text):
        self.SignUpPage = SignUpPage(self.driver)
        self.SignUpPage.input_name(name)
        self.SignUpPage.input_email(email)
        self.SignUpPage.input_password_and_confirm_password(password, confirmPassword)
        self.SignUpPage.click_signup_button()
        self.SignUpPage.assert_signup(text)