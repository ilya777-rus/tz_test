from .base_page import BasePage
from  .locators import TenzorPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class TeznzorPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_correct_url(self):
        assert self.url=="https://tensor.ru/", "url not correct !"

    def should_be_block_power_in_people(self):
        try:
            assert self.is_element_present(TenzorPageLocators.BLOCK_POWER_IN_PEOPLE), "NOT BLOCKKK"
            block_element = self.browser.find_element(*TenzorPageLocators.BLOCK_POWER_IN_PEOPLE)
            self.scroll_to_element(block_element)
        except StaleElementReferenceException as e:
            assert self.is_element_present(TenzorPageLocators.BLOCK_POWER_IN_PEOPLE), "NOT BLOCKKK"
            block_element = self.browser.find_element(*TenzorPageLocators.BLOCK_POWER_IN_PEOPLE)
            self.scroll_to_element(block_element)

    def should_be_link_detailed_click(self):
        try:
            assert self.is_element_present(TenzorPageLocators.LINK_DETAILED), "not link is detailed"
            self.pop_up_delete(TenzorPageLocators.POPUP)
            self.hide_preload_overlay()
            el = self.el_click(TenzorPageLocators.LINK_DETAILED)
            el.click()
            self.switch_to_current_window()
            assert self.browser.current_url=="https://tensor.ru/about", "not cotrrect url about"
        except StaleElementReferenceException as e:
            el = self.el_click(TenzorPageLocators.LINK_DETAILED)
            el.click()
            self.switch_to_current_window()
            assert self.browser.current_url == "https://tensor.ru/about", "not cotrrect url about"

    def hide_preload_overlay(self):
        try:
            overlay = WebDriverWait(self.browser, 6).until(
                EC.visibility_of_element_located(TenzorPageLocators.OVERLAY)
            )
            self.browser.execute_script("arguments[0].style.display = 'none';", overlay)
        except Exception as e:
            print(f"Error hiding overlay")