from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class NavigationPage(BasePage):
    NEW_ARRIVALS_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[7]/a')
    BEST_SELLERS_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[8]/a')
    BRANDS_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[9]/a/text()')
    SHIRTS_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[10]/a')
    WHITE_SHIRTS_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[11]/a')
    TIES_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[12]/a')
    GIFTING_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[13]/a')
    ACCESSORIES_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[15]')
    TROUSERS_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[16]')
    INNERWEAR_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[17]')
    POLOS_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[18]')
    COLLECTIONS_LINK = (By.XPATH, '//*[@id="idNew1"]/ul/li[19]')

    def click_new_arrivals(self):
        self.click_element(self.NEW_ARRIVALS_LINK)

    def click_best_sellers(self):
        self.click_element(self.BEST_SELLERS_LINK)

    def hover_over_brands(self):
        """Hover over the 'Brands' menu to display the submenu."""
        brands_menu = self.find_element(self.BRANDS_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(brands_menu).perform()

    def click_shirts(self):
        self.click_element(self.SHIRTS_LINK)

    def click_white_shirts(self):
        self.click_element(self.WHITE_SHIRTS_LINK)

    def click_ties(self):
        self.click_element(self.TIES_LINK)

    def click_gifting(self):
        self.click_element(self.GIFTING_LINK)

    def click_accessories(self):
        self.click_element(self.ACCESSORIES_LINK)

    def click_trousers(self):
        self.click_element(self.TROUSERS_LINK)

    def click_innerwear(self):
        self.click_element(self.INNERWEAR_LINK)

    def click_polos(self):
        self.click_element(self.POLOS_LINK)

    def click_collections(self):
        self.click_element(self.COLLECTIONS_LINK)

    def verify_menu_link(self, locator):
        """Check if a menu link is present."""
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
        except:
            return False
