##### WIP #####

import time
import allure
import pytest
from locators.locators import Live  # Ensure this contains the correct URL
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("driver")
@allure.feature("Validate new pages feature")
@allure.story("Validate newly created pages content")
@pytest.mark.usefixtures("driver")  # Using 'driver' fixture
class TestGuestCheckout:

    @allure.title("Test Guest User checkout Functionality")
    @allure.description("This test verifies that a Guest user can successfully reach PTC page.")
    def test_guest_checkout(self):
        test_name = "test_new_page_content_"  # Test case name for screenshots
        home = HomePage(self.driver)
        product = ProductPage(self.driver)
        checkout = CheckoutPage(self.driver)

        # Open the live website
        home.open_url(Live)
        time.sleep(1)
        home.capture_screenshot(test_name, "01_HomePageLoaded")  # Capture screenshot

        # Navigate to shirts section
        home.navigate_to_shirts()
        time.sleep(1)
        home.capture_screenshot(test_name, "02_NavigatedToShirts")

        # Select the first product
        product.select_first_product()
        time.sleep(1)
        product.capture_screenshot(test_name, "03_ProductPageLoaded")

        # Validate product details
        assert product.validate_product_name_and_breadcrumb(), "Mismatch between breadcrumb and product name"
        assert product.validate_swatch_images(), "Less than 2 swatch images found"

        # Select size and add to cart
        product.select_size()
        time.sleep(1)
        product.capture_screenshot(test_name, "04_SelectedSize")

        product.add_to_cart()
        time.sleep(1)
        product.capture_screenshot(test_name, "05_AddedToCart")

        # Validate cart buttons
        assert product.validate_view_cart_button(), "View Cart button is not visible"
        product.capture_screenshot(test_name, "06_ViewCartButton")

        assert product.validate_buy_now_button(), "Buy Now button not found!"
        assert product.validate_wishlist_icon(), "Wishlist icon not found!"
        assert product.validate_facebook_share(), "Facebook Share icon not found!"
        assert product.validate_whatsapp_share(), "WhatsApp Share icon not found!"

        # Click view cart and proceed to checkout
        product.click_view_cart()
        time.sleep(1)
        product.capture_screenshot(test_name, "07_ClickedViewCart")

        checkout.proceed_to_checkout()  # Use a method specific for guest checkout
        time.sleep(5)
        checkout.capture_screenshot(test_name, "08_ProceededToGuestCheckout")
