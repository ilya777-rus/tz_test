import os

from .base_page import BasePage
from .locators import ContactPageLocators
import time
from .utils import locations1, locations2, FileDownloadComplete
from selenium.common.exceptions import StaleElementReferenceException

class ContactPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_click_banner_tenzor(self):
        try:
            assert self.is_element_present(ContactPageLocators.BANNER_TENZOR), "banner tenzor is not !!!!!"
            el = self.el_click(ContactPageLocators.BANNER_TENZOR)
            el.click()
            self.switch_to_current_window()
        except StaleElementReferenceException as e:
            el = self.el_click(ContactPageLocators.BANNER_TENZOR)
            el.click()
            self.switch_to_current_window()

    def should_be_name_region(self):
        try:
            assert self.is_element_present(ContactPageLocators.REGION_SELECT), "nor region select"
            assert self.browser.find_element(
                *ContactPageLocators.REGION_SELECT).text == "Республика Башкортостан", "not is region"
            assert self.is_element_present(ContactPageLocators.CITY), "not name city region"
            assert self.browser.find_element(*ContactPageLocators.CITY).text.strip() == "Уфа", "not is UFA !"
            self.should_be_patrners(locations1)
        except StaleElementReferenceException as e:
            assert self.is_element_present(ContactPageLocators.REGION_SELECT), "nor region select"
            assert self.browser.find_element(
                *ContactPageLocators.REGION_SELECT).text == "Республика Башкортостан", "not is region"
            assert self.is_element_present(ContactPageLocators.CITY), "not name city region"
            assert self.browser.find_element(*ContactPageLocators.CITY).text.strip() == "Уфа", "not is UFA !"
            self.should_be_patrners(locations1)

    def should_be_click_region_Kamchatcka(self):
        assert self.is_element_present(ContactPageLocators.REGION_SELECT), "not region select"
        el = self.el_click(ContactPageLocators.REGION_SELECT)
        el.click()
        assert self.is_element_present(ContactPageLocators.Kamchatka), "NOT kamchatka"
        el2 = self.el_click(ContactPageLocators.Kamchatka)
        el2.click()

    def should_be_name_region_for_kamchatka(self):
        assert self.is_element_present(ContactPageLocators.REGION_SELECT), "nor region select"
        assert self.el_text_change(ContactPageLocators.REGION_SELECT,
                                   "Камчатский край"), "text not change on Kamchatcka!"
        element = self.browser.find_element(*ContactPageLocators.REGION_SELECT)
        assert element.text == "Камчатский край", "not is region"

        assert self.is_element_present(ContactPageLocators.CITY), "not name city region"
        assert self.browser.find_element(
            *ContactPageLocators.CITY).text.strip() == "Петропавловск-Камчатский", "not is Петропавловск-Камчатский !!!"
        self.should_be_patrners(locations2)

        assert self.browser.title == "СБИС Контакты — Камчатский край", "title not correct !!!!!"
        assert "41-kamchatskij-kraj" in self.browser.current_url, "kamchatsk kray not in URL !!!"

    def should_be_patrners(self, locations):
        patrners = self.browser.find_elements(*ContactPageLocators.PARTNERS)
        for i, p in enumerate(patrners[:len(locations)]):
            arr = p.text.split('\n')
            assert arr[0] == locations[i]['name'], f"current name city {arr[0]} not correct is {locations[i]['name']}"
            assert arr[1] == locations[i][
                'address'], f"current address city {arr[1]} not correct is {locations[i]['address']}"

    def click_local_versions(self):
        assert self.is_element_present(ContactPageLocators.DOWNLOAD_FILE), "not link for download file"
        element = self.el_click(ContactPageLocators.DOWNLOAD_FILE)
        self.scroll_to_element(element)
        element.click()

