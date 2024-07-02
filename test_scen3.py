
import pytest
from pages.home_page import HomePage
from pages.contact_page import ContactPage
from pages.download_page import DownloadPage

LINK = "https://sbis.ru/"

def test_scen3(browser_d):
    home_page = HomePage(browser_d, LINK)
    home_page.open()
    home_page.should_be_click_contact_link()
    contact_page = ContactPage(browser_d, browser_d.current_url)
    contact_page.click_local_versions()
    download_page = DownloadPage(browser_d, browser_d.current_url)
    download_page.should_be_download_sbis_plugin()
