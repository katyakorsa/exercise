class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.browser.get()

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def click(self, *locator):
        elem = self.browser.find_element(*locator)
        elem.click()
