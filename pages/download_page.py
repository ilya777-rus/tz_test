import os
from .home_page import HomePage
from  .locators import DownloadPageLocators

class DownloadPage(HomePage):
    def should_be_download_sbis_plugin(self):
        assert self.is_element_present(DownloadPageLocators.FILE), "not link for download file"
        elements = self.browser.find_elements(*DownloadPageLocators.FILE)
        elem=self.el_click(DownloadPageLocators.FILE,35)
        download_directory = os.getcwd()
        known_files = set(os.listdir(download_directory))

        self.scroll_to_element(elements[0])
        self.browser.execute_script("arguments[0].click();", elements[0])
        self.alert()

        new_file_path = self.complete_download_file(download_directory, known_files)
        assert os.path.isfile(new_file_path), f"File was not downloaded successfully. New file path: {new_file_path}"

        file_size_mb = self.get_file_size_in_mb(new_file_path)
        assert file_size_mb == 7.22, f"File size is {file_size_mb} MB, expected {7.22} MB."
