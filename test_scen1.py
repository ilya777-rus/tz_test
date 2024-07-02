
import time
import pytest
from pages.home_page import HomePage
from pages.tenzor_page import TeznzorPage
from pages.tenzor_about_page import TenzorAboutPage
from pages.contact_page import ContactPage

LINK = "https://sbis.ru/"

@pytest.mark.skip
def test_clcik_contact_and_banner(browser):
    home_page = HomePage(browser, LINK)
    home_page.open()
    home_page.should_be_click_contact_link()
    home_page.should_be_click_banner_tenzor()
    tenzor_page = TeznzorPage(browser, browser.current_url)
    # home_page.switch_to_current_window()
    tenzor_page.should_be_correct_url()
    tenzor_page.should_be_block()
    tenzor_page.should_be_link_detailed_click()
    tenzor_about_page = TenzorAboutPage(browser, browser.current_url)
    tenzor_about_page.should_be_work_block()
    tenzor_about_page.should_be_height_and_weight_photos_in_work_block()
    time.sleep(8)

@pytest.mark.skip
def test_scen2(browser):
    home_page = HomePage(browser, LINK)
    home_page.open()
    home_page.should_be_click_contact_link()
    contact_page=ContactPage(browser, browser.current_url)
    contact_page.should_be_name_region()
    contact_page.should_be_click_region_Kamchatcka()
    contact_page.should_be_name_region2()
    time.sleep(7)


def test_scen3(browser_d):
    home_page = HomePage(browser_d, LINK)
    home_page.open()
    home_page.should_be_click_contact_link()
    contact_page = ContactPage(browser_d, browser_d.current_url)
    contact_page.download_local_versions()


