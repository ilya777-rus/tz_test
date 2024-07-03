from .base_page import BasePage
from .locators import HomePageLocators
import time
from selenium.common.exceptions import StaleElementReferenceException

class HomePage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_click_contact_link(self):
        try:
            assert self.is_element_present(HomePageLocators.CONTACT_LINK), "contac link is not  !"
            el = self.el_click(HomePageLocators.CONTACT_LINK)
            el.click()
        except  StaleElementReferenceException as e:
            print("Erroor ", str(e))
            self.el_click(HomePageLocators.CONTACT_LINK).click()



