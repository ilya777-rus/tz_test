from  selenium.webdriver.common.by import By

class HomePageLocators:
    CONTACT_LINK = (By.CSS_SELECTOR, ".sbisru-Header__menu-item-1 > .sbisru-Header__menu-link")
    BANNER_TENZOR = (By.CSS_SELECTOR, ".sbisru-Contacts__border-left > .sbisru-Contacts__logo-tensor.mb-12 [alt='Разработчик системы СБИС — компания «Тензор»']")

class ContactPageLocators:
    REGION_SELECT = (By.CSS_SELECTOR, ".sbisru-Contacts__underline  .sbis_ru-Region-Chooser__text.sbis_ru-link")
    CITY = (By.CSS_SELECTOR, "#city-id-2")
    # PARTNERS = (By.CSS_SELECTOR, ".sbisru-Contacts-List__name")
    # PARTNERS = (By.CSS_SELECTOR, ".sbisru-Contacts-List--ellipsis.pb-xm-12")
    PARTNERS = (By.CSS_SELECTOR, ".sbisru-Contacts-List__item")
    Kamchatka = (By.CSS_SELECTOR, "[title='Камчатский край']")
    kk = (By.XPATH, "//*[text()='41 Камчатский край']")

    DOWNLOAD_FILE = (By.XPATH, "//*[text()='Скачать локальные версии']")
    FILE2 = (By.CSS_SELECTOR, ".sbis_ru-DownloadNew-flex__child:nth-child(1)  .sbis_ru-DownloadNew-loadLink__link")
    FILE1 = (By.XPATH, '//*[@id="ws-92e3gfmnar1719893517520"]/div[1]/div[2]/div[2]/div/a')
    FILE = (By.CSS_SELECTOR, ".sbis_ru-DownloadNew-block .sbis_ru-DownloadNew-loadLink .sbis_ru-DownloadNew-loadLink__link.js-link")


class TenzorPageLocators:
    BLOCK_POWER_IN_PEOPLE = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content ")
    LINK_DETAILED = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content  .tensor_ru-link.tensor_ru-Index__link")

class TenzorAboutPageLocators:
    BLOCK_WORK = (By.CSS_SELECTOR, ".tensor_ru-About__block3 .tensor_ru-About__block-title")
    PHOTOS = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image")