import unittest
from selenium import webdriver
from pages.menu_Brands_subnav import BrandsPage

class TestBrandsNavigation(unittest.TestCase):
    base_url = "https://www.zodiaconline.com/"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.base_url)
        self.brands_page = BrandsPage(self.driver)

    def test_navigate_to_brand_pages(self):
        for index in range(len(self.brands_page.brand_links)):
            self.brands_page.click_brand_link(index)
            self.assertIn(self.brands_page.brand_links[index].text.lower(), self.brands_page.get_current_url())
            self.driver.back()

    def test_brand_images_visible(self):
        for index in range(len(self.brands_page.brand_images)):
            self.assertTrue(self.brands_page.is_image_visible(index), f"Image for brand at index {index} is not visible")

    def test_brands_heading_visible(self):
        self.assertTrue(self.brands_page.brands_heading.is_displayed())
        self.assertEqual(self.brands_page.brands_heading.text, "BRANDS")

    def test_brand_names_readable(self):
        for link in self.brands_page.brand_links:
            self.assertTrue(link.is_displayed(), f"Brand link {link.text} is not readable")

    def test_active_class_on_current_brand(self):
        for index in range(len(self.brands_page.brand_links)):
            self.brands_page.click_brand_link(index)
            self.assertTrue(self.brands_page.is_active_class_present(index))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()