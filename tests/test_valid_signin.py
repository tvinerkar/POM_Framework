import pytest
import allure
import time
from pages.home_page import HomePage
from pages.signin_page import SignInPage
from locators.locators import Live

@pytest.mark.usefixtures("driver")
@allure.feature("Sign In Feature")
@allure.story("Valid Sign In")
class TestSignIn:

    @allure.title("Test Valid SignIn Functionality")
    @allure.description("This test verifies that a user can successfully log in with valid credentials.")
    def test_valid_signin(self):
        test_name = "test_valid_signin"            #test name

        home = HomePage(self.driver)
        signin = SignInPage(self.driver)

        with allure.step("Opening Home Page"):
            home.open_url(Live)
            time.sleep(1)
            home.capture_screenshot(test_name, "01_HomePageLoaded")
            time.sleep(1)
        with allure.step("Navigating to Sign In Page"):
            home.click_signin()
            time.sleep(1)
            home.capture_screenshot(test_name, "02_SignInPageLoaded")


        with allure.step("Entering Valid Credentials and Logging In"):
            signin.login("interactiveavenues43@gmail.com", "@#$Test123")
            time.sleep(1)

        with allure.step("Verifying Successful Login"):
            assert Live in self.driver.current_url, "Login failed!"
            home.capture_screenshot(test_name, "03_LoginSuccess")

