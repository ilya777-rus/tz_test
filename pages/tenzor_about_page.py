from .base_page import BasePage
from  .locators import TenzorAboutPageLocators

class TenzorAboutPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_work_block(self):
        assert self.is_element_present(TenzorAboutPageLocators.BLOCK_WORK), "block work is not !"
        block_work = self.browser.find_element(*TenzorAboutPageLocators.BLOCK_WORK)
        self.scroll_to_element(block_work)

    def should_be_height_and_weight_photos_in_work_block(self):
        assert self.is_element_present(TenzorAboutPageLocators.PHOTOS), 'not photos !'
        photos = self.browser.find_elements(*TenzorAboutPageLocators.PHOTOS)
        assert len(photos)==4, "count photos must have 4"
        first_height = photos[0].get_attribute("height")
        first_width = photos[0].get_attribute("width")

        for photo in photos[1:]:
            height = photo.get_attribute("height")
            width = photo.get_attribute("width")

            assert first_height==height, f"Разные высоты: у первой фото - {first_height} , а у текущей - {height}"
            assert first_width == width, f"Разные широты: у первой фото - {first_width} , а у текущей - {width}"