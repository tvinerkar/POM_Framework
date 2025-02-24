import time
from datetime import datetime  # Correct way
import os
import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        """Fetch text of an element identified by the locator."""
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.text.strip()
        except TimeoutException:
            return None  # Return None if element is not found

    def get_elements(self, locator):
        """Return a list of elements matching the locator."""
        try:
            return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []  # Return empty list if no elements are found

    # def capture_screenshot(self, test_name, step_name):
    #     browser_name = self.driver.capabilities['browserName']
    #     browser_version = self.driver.capabilities['browserVersion']
    #     timestamp = time.strftime("%Y%m%d_%H%M")
    #
    #     # Format: testname_step_browser_version_timestamp.png
    #     filename = f"{test_name}_{step_name}_{browser_name}_{browser_version}_{timestamp}.png"
    #
    #     # Ensure directory exists
    #     screenshot_dir = os.path.join("report", "screenshots", f"{test_name}_{timestamp}")
    #     os.makedirs(screenshot_dir, exist_ok=True)
    #
    #     # Save screenshot
    #     screenshot_path = os.path.join(screenshot_dir, filename)
    #     self.driver.save_screenshot(screenshot_path)
    #     print(f"Screenshot saved: {screenshot_path}")

    def capture_screenshot(self, test_name, step_name):
        browser_name = self.driver.capabilities['browserName']
        browser_version = self.driver.capabilities['browserVersion']
        timestamp = time.strftime("%Y%m%d_%H%M")  # Full timestamp for filenames
        date_stamp = time.strftime("%Y%m%d")  # Only date for folder naming

        filename = f"{test_name}_{step_name}_{browser_name}_{browser_version}_{timestamp}.png"

        # Base report directory
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "tests/report"))

        # 🔥 Dynamically generate directory names with the current date
        screenshot_dir = os.path.join(base_dir, f"test_guest_checkout_{date_stamp}",
                                      f"test_guest_checkout_{date_stamp}_Screenshots")

        os.makedirs(screenshot_dir, exist_ok=True)  # Ensure the directories exist

        screenshot_path = os.path.join(screenshot_dir, filename)
        self.driver.save_screenshot(screenshot_path)

        # Attach screenshot to Allure Report
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name=step_name, attachment_type=allure.attachment_type.PNG)

        print(f"Screenshot saved: {screenshot_path}")  # Debugging output



