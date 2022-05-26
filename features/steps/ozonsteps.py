from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('Website http://www.ozon.ru/')
def launchOzon(context):
    context.driver = webdriver.Chrome()
    context.driver.get('http://www.ozon.ru/')


@then('Перейти в раздел Электроника')
def launchElectronics(context):
    context.driver.find_element(By.XPATH, '//a[contains(text(), "Электроника")]').click()


@then('Перейти в подраздел Смартфоны')
def launchSmart(context):
    context.driver.find_element(By.XPATH, '//div[contains(text(), "Смартфоны")]').click()


@then('Установить фильтры по бренду')
def setBrandFilter(context):
    context.driver.find_element(By.XPATH, '//span[text()="Apple"]').click()


# @then('Сортировать товары по убыванию цены')
# def step_impl(context):
#
#
#
# @then('Выбрать первый товар и добавить в корзину')
# def step_impl(context):
#
#
#
# @then('Открыть корзину')
# def step_impl(context):
    context.driver.find_element(By.XPATH, '//a[@href="/cart"]').click()
#
#
# @then('Сравнить стоимость выбранного предмета и суммы корзины')
# def step_impl(context):