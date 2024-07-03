import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from .utils import FileDownloadComplete


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, locator, time=18):
        try:
            WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))
        except TimeoutException as e:
            print(e.msg)
            return False
        return True

    def el_click(self, locator, time=15):
        try:
            el = WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator))
            return el
        except TimeoutException as e:
            print(e.msg)
            return False

    def el_text_change(self, locator, text, time=10):
        try:
            el = WebDriverWait(self.browser, time).until(EC.text_to_be_present_in_element(locator, text))
            return el
        except TimeoutException as e:
            print('G', e.msg)
            return False

    def alert(self):
        try:
            alert = WebDriverWait(self.browser, 20).until(EC.alert_is_present())
            alert.accept()
        except TimeoutException as e:
            print("Errror alert ", str(e))

    def complete_download_file(self, download_directory, known_files, time=8):
        try:
            file_download_wait = WebDriverWait(self.browser, time).until(
                FileDownloadComplete(download_directory, known_files)
            )
            if file_download_wait:
                new_file_path = os.path.join(download_directory, file_download_wait)
            else:
                return False
        except TimeoutException as e:
            print('error', e.msg)
            return False
        return new_file_path

    def get_file_size_in_mb(self, file_path):
        size_bytes = os.path.getsize(file_path)
        size_mb = size_bytes / (1024 * 1024)  # Convert bytes to megabytes
        return round(size_mb, 2)

    def switch_to_current_window(self):
        handles = self.browser.window_handles
        self.browser.switch_to.window(handles[-1])

    def scroll_to_element(self, element):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", element)

    def pop_up_delete(self, locator):
        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located(locator)
            )

            self.browser.execute_script("""
                var element = document.getElementsByClassName('tensor_ru-CookieAgreement')[0];
                if (element) {
                    element.parentNode.removeChild(element);
                }
            """)
            print("Элемент был удален.")
        except Exception as e:
            print("Не удалось удалить элемент:", str(e))