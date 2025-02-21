import pytest
from utils.browser_factory import get_driver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.signin_page import SignInPage

@pytest.fixture(scope="class")
def driver(request):
    driver = get_driver("firefox")  # Change browser if needed
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestLoggedInCheckout:
    def test_loggedin_checkout(self):
        home = HomePage(self.driver)
        signin = SignInPage(self.driver)
        product = ProductPage(self.driver)

        home.open_url("https://preprod.zodiaconline.com/")
        home.click_signin()
        signin.login("interactiveavenues43@gmail.com", "@#$Test123")
        home.navigate_to_shirts()
        product.select_size()
        product.add_to_cart()
