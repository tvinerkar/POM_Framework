from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    CONTACT_FIELD = (By.ID, "contact")
    EMAIL_FIELD = (By.ID, "email")
    CONTINUE_BUTTON = (By.ID, "redesign-v15-cta")
    CLOSE_MODAL = (By.CSS_SELECTOR, "button.modal-close.svelte-s662vu.light-bg > svg > path")
    CONFIRM_BUTTON = (By.ID, "positiveBtn")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//button[contains(@class, 'checkout')]")  # Update if needed

    def enter_contact(self):
        self.click_element(self.CONTACT_FIELD)

    def enter_email(self, email):
        self.enter_text(self.EMAIL_FIELD, email)

    def proceed(self):
        self.click_element(self.CONTINUE_BUTTON)

    def close_modal(self):
        self.click_element(self.CLOSE_MODAL)

    def confirm_order(self):
        self.click_element(self.CONFIRM_BUTTON)

    def proceed_to_checkout(self):
        """Wait for 'Proceed to Checkout' button to be clickable, then click."""
        checkout_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.PROCEED_TO_CHECKOUT_BUTTON)
        )
        checkout_button.click()

    def verify_guest_checkout_page(self):
        """Check if the guest checkout page is loaded by verifying the presence of a key element."""
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.CONTACT_FIELD)
            )
        except:
            return False


