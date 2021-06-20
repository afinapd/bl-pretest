from selenium.webdriver.common.by import By


# constans
class Constants():
    driver = r"C:\Users\afinapd\PycharmProjects\Portfolio\chromedriver\chromedriver.exe"
    baseURL = "https://www.bukalapak.com/"


# locators
class SignUpElements():
    SIGNUP_FORM = (By.CSS_SELECTOR, ".pr-4 > .pr-4")
    ASSERT_SIGNUP_FORM = (By.CSS_SELECTOR, ".mv-48")
    FIELD_NOHP_OR_EMAIL = (By.CSS_SELECTOR, ".bl-text-field__input")
    SIGNUP_BUTTON = (By.XPATH, "//button[contains(.,'Daftar')]")
    ASSERT_WRONG_VALIDATION = (By.CSS_SELECTOR, ".bl-text--caption")
    ASSERT_VERIFICATION = (By.CSS_SELECTOR, ".mb-16")
    SEND_CODE_BUTTON = (By.CSS_SELECTOR, ".mb-8")

class SignInElements():
    SIGNIN_FORM = (By.CSS_SELECTOR, ".te-header-login > .pr-4")
    ASSERT_SIGNIN_FORM = (By.CSS_SELECTOR, ".heading > span")
    FIELD_USERNAME = (By.ID, "user_session_username")
    FIELD_PASSWORD = (By.ID, "user_session_password")
    SIGNIN_BUTTON = (By.NAME, "commit")
    ASSERT_SIGNIN = (By.CSS_SELECTOR, ".bl-avatar")

class SearchElements():
    FIELD_SEARCH = (By.ID, "v-omnisearch__input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".v-omnisearch__submit-icon")
    DELETE_SEARCH = (By.CSS_SELECTOR, ".delete-icon > use")
    ASSERT_SEARCH = (By.XPATH, "/html/body/div[2]/div/section/div/div/h1/b")

class AddToCartElements():
    PRODUCT_1 = (By.CSS_SELECTOR, ".bl-flex-item:nth-child(1) .bl-product-card__description-name .bl-link")
    ADD_CART_BUTTON = (By.CSS_SELECTOR, ".c-main-product__action__cart")
    DIALOG_CART = (By.CSS_SELECTOR, ".c-dialog__panel__title")
    SEE_CART = (By.CSS_SELECTOR, ".c-cart-dialog__cart-button")
    ASSERT_CART = (By.CSS_SELECTOR, ".bl-text--subheading-1")