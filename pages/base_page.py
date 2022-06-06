from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

locator = ('', '')

class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.timeout = timeout
        self.browser.get(url)

    def get(self, url):
        self.browser.get(url)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def find_element(self, timeout=10, locator):
        element = None

        try:
            element = WebDriverWait(self, browser, timeout).until(
                EC.presence_of_element_located(self.locator))
        except:
            print('Element is not found')
        return element

    def get_text(self):
        element = self.find_element()
        text = ''

        try:
            text = str(element.text)
        except Exception as e:
            print('Error', str(e))
        return text


    def scroll_to_element(self):
        element = self.find_element()

        try:
            element.send_keys(Keys.DOWN)
        except Exception as e:
            pass