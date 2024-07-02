from .base_page import BasePage
from  .locators import TenzorPageLocators

class TeznzorPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_correct_url(self):
        print(self.url)
        assert self.url=="https://tensor.ru/", "url not correct !!!!!"

    def should_be_block(self):
        assert self.is_element_present(TenzorPageLocators.BLOCK_POWER_IN_PEOPLE), "NOT BLOCKKK"
        block_element = self.browser.find_element(*TenzorPageLocators.BLOCK_POWER_IN_PEOPLE)
        self.browser.execute_script("return arguments[0].scrollIntoView();",block_element)

    def should_be_link_detailed_click(self):
        assert self.is_element_present(TenzorPageLocators.LINK_DETAILED), "not link is detailed"
        self.browser.find_element(*TenzorPageLocators.LINK_DETAILED).click()
        self.switch_to_current_window()
        print('xxxxxxxxx',self.browser.current_url)
        assert self.browser.current_url=="https://tensor.ru/about", "Nottttttt abouuttttttt"