from selenium import webdriver
from app.application import Application

url = 'https://www.ozon.ru/'

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.get(url)
    context.driver.implicitly_wait(10)
    context.app = Application(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()