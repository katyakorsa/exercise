from pages.base import Page
from pages.ozon import SearchPage

class Application:

    def __init__(self, driver):
        self.base = Page(driver)
        self.ozon = SearchPage(driver)





