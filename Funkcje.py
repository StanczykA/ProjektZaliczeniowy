from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

def make_screenshot(driver):
    today = datetime.datetime.today()
    short_date = today.strftime('_ekranu%H%M%S')
    screen_name = 'C:\\Users\\Adrian\\PycharmProjects\\' + 'zrzut' + short_date + '.png'
    driver.get_screenshot_as_file(screen_name)

class Logowanie:
    def __init__(self, driver):
        self.driver = driver
        self.username_field_id = 'user-name'
        self.password_field_id = 'password'
        self.login_button_name = 'login-button'

    def open(self):
        self.driver.get('https://skleptest.pl/my-account/')
        self.driver.maximize_window()

    def enter_username(self, username):
        field = self.driver.find_element(By.XPATH,'//*[@id="username"]')
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        field.send_keys(password)

    def click_login(self):
        button = self.driver.find_element(By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
        button.click()


class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
