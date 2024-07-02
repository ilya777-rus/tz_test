import os

from .base_page import BasePage
from .locators import  ContactPageLocators
import time
from .utils import locations1, locations2, FileDownloadComplete

class ContactPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_click_banner_tenzor(self):
        assert self.is_element_present(ContactPageLocators.BANNER_TENZOR), "banner tenzor is not !!!!!"
        el = self.el_click(ContactPageLocators.BANNER_TENZOR)
        el.click()
        self.switch_to_current_window()

    def should_be_name_region(self):
        # time.sleep(2)
        assert self.is_element_present(ContactPageLocators.REGION_SELECT), "nor region select"
        print(self.browser.find_element(*ContactPageLocators.REGION_SELECT).text)
        assert self.browser.find_element(*ContactPageLocators.REGION_SELECT).text== "Республика Башкортостан", "not is regionnn"

        assert self.is_element_present(ContactPageLocators.CITY), "not name city region"
        assert self.browser.find_element(*ContactPageLocators.CITY).text.strip()=="Уфа", "not is UFA !!!"
        print(self.browser.find_element(*ContactPageLocators.CITY).text)
        patrners = self.browser.find_elements(*ContactPageLocators.PARTNERS)
        ar = []
        for i,p in enumerate( patrners[:12]):
            arr=p.text.split('\n')
            assert arr[0]==locations1[i]['name'], f"current name city {arr[0]} not correct is {locations1[i]['name']}"
            assert arr[1] == locations1[i]['address'], f"current address city {arr[1]} not correct is {locations1[i]['address']}"
            print(p.text.split('\n'))
            ar.append({})
            # if i%2!=0:
            print('---------------------')

    def should_be_click_region_Kamchatcka(self):
        print('zxxxxxxxxxxxxxxx')
        assert self.is_element_present(ContactPageLocators.REGION_SELECT), "nor region select"
        print(self.browser.find_element(*ContactPageLocators.REGION_SELECT).text)

        self.browser.find_element(*ContactPageLocators.REGION_SELECT).click()
        assert self.is_element_present(ContactPageLocators.Kamchatka), "NOT kamchatka"

        # time.sleep(12)
        # print(self.browser.find_element(*ContactPageLocators.kk).text)
        print('cvvvvvvvvvvvv')
        el=self.el_click(ContactPageLocators.Kamchatka)
        el.click()
        # self.browser.find_element(*ContactPageLocators.kk).click()
        # time.sleep(2)

    def should_be_name_region2(self):


        assert self.is_element_present(ContactPageLocators.REGION_SELECT), "nor region select"
        assert self.el_text_change(ContactPageLocators.REGION_SELECT, "Камчатский край"), "NOT TEXT IN PRESENTTTT"

        print('cccccccccccccccccc should_be_name_region2',self.browser.find_element(*ContactPageLocators.REGION_SELECT).text)
        assert self.browser.find_element(*ContactPageLocators.REGION_SELECT).text== "Камчатский край", "not is 22222regionnn"

        assert self.is_element_present(ContactPageLocators.CITY), "not name city region"
        assert self.browser.find_element(*ContactPageLocators.CITY).text.strip()=="Петропавловск-Камчатский", "not is Петропавловск-Камчатский !!!"
        print(self.browser.find_element(*ContactPageLocators.CITY).text)
        patrners = self.browser.find_elements(*ContactPageLocators.PARTNERS)
        for i,p in enumerate( patrners):
            arr=p.text.split('\n')
            assert arr[0]==locations2[i]['name'], f"current name city {arr[0]} not correct is {locations2[i]['name']}"
            assert arr[1] == locations2[i]['address'], f"current address city {arr[1]} not correct is {locations2[i]['address']}"
            # print(p.text.split('\n'))

            # if i%2!=0:
            # print('---------------------')

        print('Titleeeeeeeeeeeeeeeeeeeeeeeee')
        # self.switch_to_current_window()
        print(self.browser.current_url)
        print(self.browser.title)
        assert self.browser.title == "СБИС Контакты — Камчатский край", "title not correct !!!!!"
        assert "41-kamchatskij-kraj" in self.browser.current_url, "kamchatsk kray not in URL !!!"

    def download_local_versions(self):
        assert self.is_element_present(ContactPageLocators.DOWNLOAD_FILE), "not link for download file"
        element = self.el_click(ContactPageLocators.DOWNLOAD_FILE)
        self.browser.execute_script("return arguments[0].scrollIntoView();", element)
        element.click()
        # self.switch_to_current_window()
        assert self.is_element_present(ContactPageLocators.FILE), "sxzcccccccccc"
        # self.is_element_present(ContactPageLocators.FILE).click()
        ee = self.browser.find_elements(*ContactPageLocators.FILE)
        elem=self.el_click(ContactPageLocators.FILE,35)
        print('ELEMMMMMMMMMMMM,', elem)
        # print(ee[0].get_attribute())
        # self.browser.implicitly_wait(7)
        download_directory = os.getcwd()
        print('TESTTTTTTTTTTTTTTTTTTTTTTTTT', download_directory)
        known_files = set(os.listdir(download_directory))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", ee[0])
        self.browser.execute_script("arguments[0].click();", ee[0])
        self.alert()
        # time.sleep(31)
        print('xxxxxxxxxx',ee)
        new_file_path = self.complete_download_file(download_directory, known_files)
        assert os.path.isfile(new_file_path), f"File was not downloaded successfully. New file path: {new_file_path}"

        file_size_mb = self.get_file_size_in_mb(new_file_path)
        print('file_size_mbbbbbbbbbbbbbb', file_size_mb)
        assert file_size_mb == 7.22, f"File size is {file_size_mb} MB, expected {7.22} MB."
        # ee[0].click()
        # time.sleep(25)