from pages.base_page import BasePage
from locators import AllLocators


class MainPage(BasePage):
    def __init__(self, browser, url=''):
        url = 'https://www.ozon.ru/'
        super.__init__(browser, url)

    electronics_search = BasePage(*AllLocators.ELECTRONICS)
    smartphones_search = BasePage(*AllLocators.SMARTPHONES)
    filter_by_brand = BasePage(*AllLocators.BRAND_FILTER)
    sort_by_price = BasePage(*AllLocators)
    add_to_cart_button = BasePage(*AllLocators.ADD_TO_CART)
    go_to_cart = BasePage(*AllLocators.CART)
    products_prices = BasePage