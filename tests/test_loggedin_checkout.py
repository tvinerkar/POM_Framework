from gevent.testing.monkey_test import test_name
from utils.browser_factory import get_driver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.signin_page import SignInPage
import time
import pytest
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage
import sys
import os

# Ensure the project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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
        time.sleep(1)
        home.capture_screenshot(test_name, "01_HomePageLoaded")  # Capture screenshot

        home.click_signin()
        time.sleep(1)
        home.capture_screenshot(test_name, "02_SignInPageLoaded")  # Capture screenshot

        signin.login("interactiveavenues43@gmail.com", "@#$Test123")
        time.sleep(1)
        home.capture_screenshot(test_name, "03_Username_Password")  # Capture screenshot

        home.navigate_to_shirts()
        time.sleep(1)
        home.capture_screenshot(test_name, "02_NavigatedToShirts")

        product.select_first_product()
        time.sleep(1)
        product.capture_screenshot(test_name, "03_ProductPageLoaded")

        assert product.validate_product_name_and_breadcrumb(), "Mismatch between breadcrumb and product name"
        assert product.validate_swatch_images(), "Less than 2 swatch images found"

        product.select_size()
        time.sleep(1)
        product.capture_screenshot(test_name, "04_SelectedSize")

        product.add_to_cart()
        time.sleep(1)
        product.capture_screenshot(test_name, "05_AddedToCart")

        assert product.validate_view_cart_button(), "View Cart button is not visible"
        product.capture_screenshot(test_name, "06_ViewCartButton")

        assert product.validate_buy_now_button(), "Buy Now button not found!"

        assert product.validate_wishlist_icon(), "Wishlist icon not found!"

        assert product.validate_facebook_share(), "Facebook Share icon not found!"

        assert product.validate_whatsapp_share(), "WhatsApp Share icon not found!"

        product.click_view_cart()
        time.sleep(1)
        product.capture_screenshot(test_name, "07_ClickedViewCart")

        checkout.proceed_to_checkout()
        time.sleep(5)
        checkout.capture_screenshot(test_name, "08_ProceededToCheckout")

        product.select_size()
        product.add_to_cart()
