from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class BrandsPage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def brands_heading(self):
        return self.driver.find_element_by_css_selector("h3")

    @property
    def brand_links(self):
        return self.driver.find_elements_by_css_selector(".secondLevelSubNav a")

    @property
    def brand_images(self):
        return self.driver.find_elements_by_css_selector(".brands-subnav img")

    def click_brand_link(self, index):
        self.brand_links[index].click()

    def get_current_url(self):
        return self.driver.current_url

    def is_image_visible(self, index):
        return self.brand_images[index].is_displayed()

    def is_active_class_present(self, index):
        return 'active' in self.brand_links[index].get_attribute('class')