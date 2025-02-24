import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignInPage(BasePage):
    EMAIL_FIELD = (By.ID, "mobilenumber")
    PASSWORD_FIELD = (By.ID, "login_password")
    LOGIN_BUTTON = (By.ID, "fwithotp")
    EMAIL_RADIO_BUTTON= (By.ID,"logtypeboxemail")
    SUBMIT_CTA = (By.ID,"fchknum")

    def login(self, email, password):
        self.click_element(self.EMAIL_RADIO_BUTTON)
        time.sleep(1)
        self.enter_text(self.EMAIL_FIELD, email)
        time.sleep(1)
        self.click_element(self.SUBMIT_CTA)
        time.sleep(1)
        self.enter_text(self.PASSWORD_FIELD, password)
        time.sleep(1)
        self.click_element(self.LOGIN_BUTTON)
        time.sleep(1)
