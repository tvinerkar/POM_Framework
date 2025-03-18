import time
import allure
import pytest
from pages.menu_navigation_objects import NavigationPage
from utils.browser_factory import get_driver
from pages.home_page import HomePage
@pytest.mark.usefixtures("driver")
@allure.feature("Validate menu links Feature")
@allure.story("Validate menu links journey")
class TestMenuLinks:
    test_name = "test_menu_links"  # Define a global test name for screenshots
    #date_stamp = time.strftime("%Y%m%d")  # Only date for folder naming
    def test_open_homepage(self, date_stamp=time.strftime("%Y%m%d")):
        #self.driver = get_driver("chrome")  # Ensure driver is initialized
        self.navigation_page = NavigationPage(self.driver)
        home = HomePage(self.driver)
        self.driver.get("https://zodiaconline.com/")

        home.capture_screenshot(self.test_name, "01_HomePageLoaded")


        self.navigation_page.click_new_arrivals()
        assert self.driver.current_url == "https://www.zodiaconline.com/new-arrivals"
        time.sleep(1)
        self.navigation_page.capture_screenshot(self.test_name, "02_NewArrivals_page_Loaded")


        self.navigation_page.click_best_sellers()
        assert self.driver.current_url == "https://www.zodiaconline.com/best-sellers"
        time.sleep(1)
        self.navigation_page.capture_screenshot(self.test_name, "03_Best_sellers_page_Loaded")


#        self.navigation_page.hover_over_brands()

        self.navigation_page.click_shirts()
        assert self.driver.current_url == "https://www.zodiaconline.com/shirts"
        time.sleep(1)
        self.navigation_page.capture_screenshot(self.test_name, "03_Shirts_page_Loaded")

        self.navigation_page.click_white_shirts()
        assert self.driver.current_url == "https://www.zodiaconline.com/shirts/white-shirts"
        time.sleep(1)
        self.navigation_page.capture_screenshot(self.test_name, "04_White_Shirts_page_Loaded")

        self.navigation_page.click_ties()
        assert self.driver.current_url == "https://www.zodiaconline.com/ties"
        time.sleep(1)
        self.navigation_page.capture_screenshot(self.test_name, "05_Ties_page_Loaded")

        self.navigation_page.click_gifting()
        assert self.driver.current_url == "https://www.zodiaconline.com/gifting"
        time.sleep(1)
        self.navigation_page.capture_screenshot(self.test_name, "06_Gifting_page_Loaded")

        self.navigation_page.click_accessories()
        assert self.driver.current_url == "https://www.zodiaconline.com/accessories"
        time.sleep(1)
        self.navigation_page.capture_screenshot(self.test_name, "07_accessories_page_Loaded")

        self.navigation_page.click_trousers()
        assert self.driver.current_url == "https://www.zodiaconline.com/trousers"
        time.sleep(1)
        self.navigation_page.capture_screenshot(self.test_name, "08_trousers_page_Loaded")

        self.navigation_page.click_innerwear()
        assert self.driver.current_url == "https://www.zodiaconline.com/innerwear"
        time.sleep(1)
        self.navigation_page.capture_screenshot(self.test_name, f"{date_stamp}_09_innerwear_page_Loaded")


        self.navigation_page.click_polos()
        assert self.driver.current_url == "https://www.zodiaconline.com/polo-tshirts"
        time.sleep(1)
        self.navigation_page.capture_screenshot(self.test_name, "10_polo-tshirts_page_Loaded")

        self.navigation_page.click_collections()
        assert self.driver.current_url == "https://www.zodiaconline.com/collection"
        time.sleep(1)
        self.navigation_page.capture_screenshot(self.test_name, "11_collection_page_Loaded")



