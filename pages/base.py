class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        elem = self.driver.find_element(*locator)
        elem.click()

    # def verify_price(self, price, *locator):
    #     result_sum = self.driver.find_element(*locator).text
    #     assert price in result_sum, f"Стоимость предмета совпадает с {result_sum}"
