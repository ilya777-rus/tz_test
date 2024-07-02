
import time
import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage


LINK = "https://sbis.ru/"

def test_scen2(browser):
    home_page = HomePage(browser, LINK)
    home_page.open()
    home_page.should_be_click_contact_link()
    contact_page=ContactPage(browser, browser.current_url)
    contact_page.should_be_name_region()
    contact_page.should_be_click_region_Kamchatcka()
    contact_page.should_be_name_region_for_kamchatka()
    time.sleep(7)