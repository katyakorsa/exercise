from selenium.webdriver.common.by import By


class AllLocators(object):
    ELECTRONICS = (By.XPATH, '//a[contains(text(), "Электроника")]')
    SMARTPHONES = (By.XPATH, '//div[contains(text(), "Смартфоны")]')
    BRAND_FILTER = (By.XPATH, '(//span[contains(text(), "Apple")])[1]')
    PRICE = (By.XPATH, '//div[@text="Популярные"]')
    PRICE_DESC = (By.XPATH, '//div[@text="Сначала дорогие"]')
    ADD_TO_CART = (By.XPATH, '(//span[text()="В корзину"])[1]')
    CART = (By.XPATH, '//a[@href="/cart"]')
    ALL_ITEM = (By.XPATH, '//span[contains(text(), "Общая стоимость")]')
    ITEM = (By.XPATH, '//span[text()="Товары (1)"]')
