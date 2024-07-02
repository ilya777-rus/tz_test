from .base_page import BasePage
from .locators import HomePageLocators
import time

class HomePage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_click_contact_link(self):
        try:
            assert self.is_element_present(HomePageLocators.CONTACT_LINK), "contacl link not is !!!!"
            el=self.el_click(HomePageLocators.CONTACT_LINK)
            el.click()
        except Exception as e:
            print('ERRORRRRRRRRRRRRR', str(e))

    def should_be_click_banner_tenzor(self):
        assert self.is_element_present(HomePageLocators.BANNER_TENZOR), "banner tenzor is not !!!!!"
        self.browser.find_element(*HomePageLocators.BANNER_TENZOR).click()
        self.switch_to_current_window()
        time.sleep(1)
        # print(self.browser.current_url)
        # assert self.browser.current_url=="https://tensor.ru", "url not correct !!!!!"

    def should_be_correct_url(self, link):
        print(link)
        assert link=="https://tensor.ru/", "url not correct !!!!!"


