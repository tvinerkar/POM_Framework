from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SHIRTS_CATEGORY = (By.LINK_TEXT, "SHIRTS")
    SIGNIN_BUTTON = (By.LINK_TEXT, "Sign In / Register")
    LOGIN_DROPDOWN = (By.XPATH,"//li/i")

    def navigate_to_shirts(self):
        self.click_element(self.SHIRTS_CATEGORY)

    def click_signin(self):
        self.click_element(self.LOGIN_DROPDOWN)
        self.click_element(self.SIGNIN_BUTTON)
