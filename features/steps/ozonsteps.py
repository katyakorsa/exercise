from behave import *
from selenium import webdriver
# from env.environment import Environment


@step('Открыть страницу "{url}"')
def load(context, url):
    context.browser = webdriver.Chrome()
    context.browser.get(url)


# @step('Перейти в раздел Электроника')
# def get_electronics(context):
#     context.env.main_page.get_item()


# @step('Перейти в подраздел Смартфоны')
# def get_smartphones(context):
#     context.driver.find_element(*AllLocators.SMARTPHONES).click()

#
# @step('Установить фильтры по бренду Apple')
# def set_brand_filter(context):
#     context.driver.find_element(*AllLocators.BRAND_FILTER).click()


# @step('Сортировать товары по убыванию цены')
# def sort_price_desc(context):
#     context.driver.find_element(*AllLocators.PRICE_DESC).click()


# @step('Выбрать первый товар и добавить в корзину')
# def step_impl(context):
#     context.driver.find_element(*AllLocators.CHOOSE_ITEM).click()
#
#
# @step('Открыть корзину')
# def open_cart(context):
#     context.driver.find_element(*AllLocators.CART).click()


# @step('Сравнить стоимость выбранного предмета и суммы корзины')
# def step_impl(context):
#     item = context.driver.find_element(*AllLocators.ITEM)
#     all_item = context.driver.find_element(*AllLocators.ALL_ITEM)
#     if item == all_item:
#         assert True, "Стоимость и сумма совпадают"
#     else:
#         assert False, "Стоимость и сумма не совпадают"
