import sys
import os
import time
import allure
import pytest

# Ensure the project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.browser_factory import get_driver
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.signin_page import SignInPage
from pages.checkout_page import CheckoutPage


@pytest.mark.usefixtures("driver")
@allure.feature("Logged in checkout Feature")
@allure.story("Valid logged-in user checkout journey")
class TestLoggedInCheckout:

    @allure.title("Test Valid Checkout Functionality")
    @allure.description("This test verifies that a user can successfully reach PTC page with valid credentials.")
    def test_loggedin_checkout(self):
        test_name = "test_loggedin_checkout"
        home = HomePage(self.driver)
        signin = SignInPage(self.driver)
        product = ProductPage(self.driver)
        checkout = CheckoutPage(self.driver)

        # Open the website
        home.open_url("https://preprod.zodiaconline.com/")
        time.sleep(1)
        home.capture_screenshot(test_name, "01_HomePageLoaded")

        # Click Sign-In
        home.click_signin()
        time.sleep(1)
        home.capture_screenshot(test_name, "02_SignInPageLoaded")

        # Perform Login
        signin.login("interactiveavenues43@gmail.com", "@#$Test123")
        time.sleep(1)
        home.capture_screenshot(test_name, "03_LoggedIN")

        # Navigate to Shirts
        home.navigate_to_shirts()
        time.sleep(1)
        home.capture_screenshot(test_name, "04_NavigatedToShirts")

        # Select First Product
        product.select_first_product()
        time.sleep(1)
        product.capture_screenshot(test_name, "05_ProductPageLoaded")

        # Assertions for Product Page
        assert product.validate_product_name_and_breadcrumb(), "Mismatch between breadcrumb and product name"
        assert product.validate_swatch_images(), "Less than 2 swatch images found"

        # Select Size and Add to Cart
        product.select_size()
        time.sleep(1)
        product.capture_screenshot(test_name, "06_SelectedSize")

        product.add_to_cart()
        time.sleep(1)
        product.capture_screenshot(test_name, "07_AddedToCart")

        # Validate Cart and Checkout
        assert product.validate_view_cart_button(), "View Cart button is not visible"
        product.capture_screenshot(test_name, "08_ViewCartButton")

        assert product.validate_buy_now_button(), "Buy Now button not found!"
        assert product.validate_wishlist_icon(), "Wishlist icon not found!"
        assert product.validate_facebook_share(), "Facebook Share icon not found!"
        assert product.validate_whatsapp_share(), "WhatsApp Share icon not found!"

        # Proceed to Checkout
        product.click_view_cart()
        time.sleep(1)
        product.capture_screenshot(test_name, "09_ClickedViewCart")

        checkout.proceed_to_checkout()
        time.sleep(5)
        checkout.capture_screenshot(test_name, "10_ProceededToCheckout")
