import unittest
from appium import webdriver

from tests_mobile.Pages import SignInPage, SignUpPage


class AppStart(unittest.TestCase):
    @classmethod
    def setUp(self):
        app = {
            "deviceName": "ce9068947d84",
            "platformName": "Android",
            "app": r"C:\Users\afinapd\PycharmProjects\bukalapak\tests_mobile\Sample Android App Login Test_v4.0_apkpure.com.apk",
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", app)
        self.driver.implicitly_wait(20)
        self.SignInPage = SignInPage(self.driver)
        self.SignUpPage = SignUpPage(self.driver)

    @classmethod
    def tearDown(self):
        self.driver.quit()


    def test_signin_success(self):
        self.SignInPage.click_signup_menu()
        self.SignUpPage.user_signup("test", "afinapd03@gmail.com", "afina123", "afina123", "Registration Successful")
        self.SignUpPage.click_signin_menu()
        self.SignInPage.input_email("afinapd03@gmail.com")
        self.SignInPage.input_password("afina123")
        self.SignInPage.click_signin_button()
        self.SignInPage.assert_signin_success()

    def test_signin_failed(self):
        self.SignInPage.input_email("afinapd03@gmail.com")
        self.SignInPage.input_password("test1234")
        self.SignInPage.click_signin_button()
        self.SignInPage.assert_signin_failed()

    def test_signup_success(self):
        self.SignInPage.click_signup_menu()
        self.SignUpPage.input_name("test")
        self.SignUpPage.input_email("afinapd03@gmail.com")
        self.SignUpPage.input_password_and_confirm_password("afina123", "afina123")
        self.SignUpPage.click_signup_button()
        self.SignUpPage.assert_signup("Registration Successful")

    def test_signup_failed(self):
        self.SignInPage.click_signup_menu()
        # user sign up
        self.SignUpPage.user_signup("test", "afinapd03@gmail.com", "afina123", "afina123", "Registration Successful")
        # user sign up again
        self.SignUpPage.input_name("test")
        self.SignUpPage.input_email("afinapd03@gmail.com")
        self.SignUpPage.input_password_and_confirm_password("afina123", "afina123")
        self.SignUpPage.click_signup_button()
        self.SignUpPage.assert_signup("Email Already Exists")

    def test_scenario_signup_signin(self):
        # user sign up
        self.SignInPage.click_signup_menu()
        self.SignUpPage.user_signup("test", "afinapd03@gmail.com", "afina123", "afina123", "Registration Successful")
        # user sign in
        self.SignUpPage.click_signin_menu()
        self.SignInPage.user_signin("afinapd03@gmail.com", "afina123")

if __name__ == '__main__':
    unittest.main()
