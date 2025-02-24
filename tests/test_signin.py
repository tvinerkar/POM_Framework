# import time
# import pytest
# from pages.home_page import HomePage
# from pages.signin_page import SignInPage
# import sys
# import os
#
# # Ensure the project root is in sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
#
# @pytest.mark.usefixtures("driver")  # Using 'driver' fixture from conftest.py
# class TestSignIn:
#     def test_valid_signin(self):
#         test_name = "test_signin"  # Define test case name
#         home = HomePage(self.driver)
#         signin = SignInPage(self.driver)
#
#         home.open_url("https://preprod.zodiaconline.com/")
#         time.sleep(1)
#         home.capture_screenshot(test_name, "01_HomePageLoaded")
#
#         home.click_signin()
#         time.sleep(1)
#         home.capture_screenshot(test_name, "02_SignInPageLoaded")
#
#         signin.login("interactiveavenues43@gmail.com", "@#$Test123")
#         time.sleep(1)
#         home.capture_screenshot(test_name, "03_Username_Password")
#
#         # Verify if login was successful
#         assert "https://preprod.zodiaconline.com" in self.driver.current_url, "Login failed!"
#         home.capture_screenshot(test_name, "04_LoginSuccess")


import pytest
import allure
import time
from pages.home_page import HomePage
from pages.signin_page import SignInPage


@pytest.mark.usefixtures("driver")
@allure.feature("Sign In Feature")
@allure.story("Valid Sign In")
class TestSignIn:

    @allure.title("Test Valid SignIn Functionality")
    @allure.description("This test verifies that a user can successfully log in with valid credentials.")
    def test_valid_signin(self):
        test_name = "test_valid_signin"

        home = HomePage(self.driver)
        signin = SignInPage(self.driver)

        with allure.step("Opening Home Page"):
            home.open_url("https://preprod.zodiaconline.com/")
            time.sleep(1)
            home.capture_screenshot(test_name, "01_HomePageLoaded")

        with allure.step("Navigating to Sign In Page"):
            home.click_signin()
            time.sleep(1)
            home.capture_screenshot(test_name, "02_SignInPageLoaded")

        with allure.step("Entering Valid Credentials and Logging In"):
            signin.login("interactiveavenues43@gmail.com", "@#$Test123")
            time.sleep(1)
            home.capture_screenshot(test_name, "03_Username_Password")

        with allure.step("Verifying Successful Login"):
            assert "https://preprod.zodiaconline.com/" in self.driver.current_url, "Login failed!"
            home.capture_screenshot(test_name, "04_LoginSuccess")
