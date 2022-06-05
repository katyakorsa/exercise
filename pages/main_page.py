from base_page import BasePage
from locators import AllLocators


class MainPage(BasePage):
    def get_item(self):
        self.find_element(*AllLocators.ЭЛЕКТРОНИКА)
        self.click(*AllLocators.ЭЛЕКТРОНИКА)

    def get_smartphones(self):
        self.click(*AllLocators.SMARTPHONES)

    # def verify_search_result(self, search_text: str):
    #     result_text = self.find_element(*AllLocators.locator).text
    #     assert search_text in result_text, f"Стоимость '{search_text}' выбранного товара " \
    #                                        f"совпадает с '{result_text}' - суммой корзины"
