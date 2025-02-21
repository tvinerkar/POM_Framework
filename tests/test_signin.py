import pytest
from utils.browser_factory import get_driver
from pages.home_page import HomePage
from pages.signin_page import SignInPage

@pytest.fixture(scope="class")
def driver(request):
    driver = get_driver("chrome")  # Change to "firefox" or "edge" if needed
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestSignIn:
    def test_valid_signin(self):
        home = HomePage(self.driver)
        signin = SignInPage(self.driver)

        home.open_url("https://preprod.zodiaconline.com/")
        home.click_signin()
        signin.login("interactiveavenues43@gmail.com", "@#$Test123")

        # Verify if login was successful
        assert "customer/account" in self.driver.current_url, "Login failed!"
