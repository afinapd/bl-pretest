from selenium.webdriver.common.by import By

# locators
class SignInElements():
    FIELD_EMAIL = (By.ID, "com.loginmodule.learning:id/textInputEditTextEmail")
    FIELD_PASSWORD = (By.ID, "com.loginmodule.learning:id/textInputEditTextPassword")
    SIGNIN_BUTTON = (By.ID, "com.loginmodule.learning:id/appCompatButtonLogin")
    ASSERT_SNACKBAR = (By.ID, "com.loginmodule.learning:id/snackbar_text")
    ASSERT_SIGNIN_SUCCESS = (By.CLASS_NAME, "android.widget.TextView")
    SIGNUP_MENU = (By.ID, "com.loginmodule.learning:id/textViewLinkRegister")

class SignUpElements():
    FIELD_NAME = (By.ID, "com.loginmodule.learning:id/textInputEditTextName")
    FIELD_EMAIL = (By.ID, "com.loginmodule.learning:id/textInputEditTextEmail")
    FIELD_PASSWORD = (By.ID, "com.loginmodule.learning:id/textInputEditTextPassword")
    FIELD_CONFIRM_PASSWORD =(By.ID, "com.loginmodule.learning:id/textInputEditTextConfirmPassword")
    SIGNUP_BUTTON = (By.ID, "com.loginmodule.learning:id/appCompatButtonRegister")
    ASSERT_SNACKBAR = (By.ID, "com.loginmodule.learning:id/snackbar_text")
    ASSERT_SIGNIN_SUCCESS = (By.CLASS_NAME, "android.widget.TextView")
    SIGNIN_MENU = (By.ID, "com.loginmodule.learning:id/appCompatTextViewLoginLink")