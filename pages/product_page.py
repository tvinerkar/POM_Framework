from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException  # Import this

from pages.base_page import BasePage


class ProductPage(BasePage):
    FIRST_PRODUCT = (By.XPATH, "(//li[contains(@class, 'product-item')])[1]//a[@class='product-item-link']")
    SIZE_OPTION = (By.ID, "option-label-size-153-item-270")
    ADD_TO_CART = (By.XPATH, "//button[@id='product-addtocart-button']/span")
    VIEW_CART = (By.XPATH, "//button[@id='product-addtocart-button']/span")
    BUY_NOW = (By.XPATH, "//button[@id='product-sparsh-buynow-button']")
    WISHLIST_ICON = (By.CSS_SELECTOR, "button.action.towishlist")
    FACEBOOK_SHARE = (By.XPATH, "//a[contains(@class,'facebookS')]")
    WHATSAPP_SHARE = (By.XPATH, "//a[contains(@class,'whatsup')]")
    BREADCRUMB_LAST_ITEM = (By.XPATH, "//ul[@class='items breadcrumb']/li[last()]/span")
    PRODUCT_NAME = (By.XPATH, "//h1[@class='product-name']")
    SWATCH_IMAGES = (By.XPATH, "//div[contains(@class, 'swatch-attribute-options')]//div[contains(@class, 'swatch-option')]")

    def select_first_product(self):
        self.click_element(self.FIRST_PRODUCT)

    def select_size(self):
        self.click_element(self.SIZE_OPTION)

    def add_to_cart(self):
        self.click_element(self.ADD_TO_CART)

    def click_view_cart(self):
        self.click_element(self.VIEW_CART)

    def validate_view_cart_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.VIEW_CART)
        )

    def validate_buy_now_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.BUY_NOW)
        )

    def validate_wishlist_icon(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.WISHLIST_ICON)
            )
        except TimeoutException:
            return False  # More precise exception handling

    def validate_facebook_share(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.socialIcon.facebookS"))
            )
        except TimeoutException:
            return False  # More precise exception handling

    def validate_whatsapp_share(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.socialIcon.whatsup"))
            )
        except TimeoutException:
            return False

    def get_product_name(self):
        """Fetch the product name from the page."""
        return self.get_element_text(self.PRODUCT_NAME)

    def get_breadcrumb_text(self):
        """Fetch the last item in the breadcrumb."""
        return self.get_element_text(self.BREADCRUMB_LAST_ITEM)

    def count_swatch_images(self):
        """Return the number of swatch images available."""
        return len(self.get_elements(self.SWATCH_IMAGES))

    def validate_product_name_and_breadcrumb(self):
        """Check if the product name matches the breadcrumb text."""
        product_name = self.get_product_name()
        breadcrumb_text = self.get_breadcrumb_text()
        return product_name.strip() == breadcrumb_text.strip()

    def validate_swatch_images(self):
        """Check if at least 2 swatch images are present."""
        return self.count_swatch_images() >= 2
