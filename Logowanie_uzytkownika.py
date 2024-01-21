import pytest
from selenium import webdriver
from Funkcje import Logowanie
import time
from Funkcje import make_screenshot


test_data = [
    ('sta@test.pl', 'testowehaslo', 'https://skleptest.pl/my-account/'),
    ('5464356436456', '%$%&^%*&%*&%&*^&^', 'https://skleptest.pl/my-account/'),
    ('JHJLHHFLSHLFHSLFLSHFLSJHFLJSHFLJSHFLJHSJKFHSLFHLSFHSLJFHLSHF', '', 'https://skleptest.pl/my-account/'),
    ('', '', 'https://skleptest.pl/my-account/'),
    ('testowylogin', '', 'https://skleptest.pl/my-account/'),
    ('sta@test.pl', 'sapkgjasoig34hg', 'https://skleptest.pl/my-account/'),
    ('sdkajfa08su5480tq0f', 'testowehaslo', 'https://skleptest.pl/my-account/'),
]

@pytest.mark.parametrize('username, password, url', test_data)
def test_login_page(username, password, url):
    driver = webdriver.Chrome()
    page = Logowanie(driver)
    page.open()
    page.enter_username(username)
    page.enter_password(password)
    page.click_login()
    time.sleep(1)

    try:
         driver.find_element ('xpath','/html/body/div/div/div[2]/div/div/main/article/div[2]/nav/ul/li[1]/a')
         make_screenshot(driver)
    except:
        print('Logowanie nieudane')
        raise
    else:
        print('Logowanie poprawne')
    finally:
        driver.quit()