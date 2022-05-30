from pages.base import Page
from pages.locators import AllLocators

class SearchPage(Page, AllLocators):

    def launch_ozon(self):
        self.click(*self.ELECTRONICS)

    def search_smart(self):
        self.click(*self.SMARTPHONES)

    def set_filter(self):
        self.click(*self.BRAND_FILTER)
