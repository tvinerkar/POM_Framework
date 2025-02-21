from datetime import datetime  # Correct way
import os

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

    def capture_screenshot(self, test_name, step_name):
            """Captures and saves a screenshot with test name and step description."""

            # Folder timestamp: YearMonthDay_Hour (e.g., 20250221_14)
            folder_timestamp = datetime.now().strftime("%Y%m%d_%H")
            folder_name = f"C:\\Users\\tejas.vinerkar\\PycharmProjects\\POM_Framework\\report\\screenshots\\{test_name}_{folder_timestamp}"

            # Ensure directory exists
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            # Screenshot filename timestamp: screenshot name + YearMonthDay_HourMinute (e.g., 01_HomePageLoaded_20250221_1415.png)
            screenshot_timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            screenshot_path = os.path.join(folder_name, f"{step_name}_{screenshot_timestamp}.png")

            # Take screenshot
            self.driver.save_screenshot(screenshot_path)
            print(f"📸 Screenshot saved: {screenshot_path}")  # Log the screenshot path