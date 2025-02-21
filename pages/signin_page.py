from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignInPage(BasePage):
    EMAIL_FIELD = (By.ID, "mobilenumber")
    PASSWORD_FIELD = (By.ID, "login_password")
    LOGIN_BUTTON = (By.ID, "fwithotp")

    def login(self, email, password):
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)
