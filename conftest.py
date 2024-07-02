import pytest
from selenium import webdriver
import os


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture(scope='function')
def browser_d():
    current_directory = os.getcwd()
    print("Текущий рабочий каталог:", current_directory)
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": current_directory,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--safebrowsing-disable-download-protection")
    browser = webdriver.Chrome(options=options)
    yield browser
    print('ssssssss')
    browser.quit()