from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Funkcje import make_screenshot
from Funkcje import bcolors
import time
import pytest

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://skleptest.pl/')

try:
    account = driver.find_element('xpath','/html/body/div/header[1]/div/div/div/ul/li[3]/a')
    account.click()
except:
    print(bcolors.FAIL + ' Test 1 Niepoprawnie otworzono okno rejestracji - FAILED ')
    raise
else:
    print(bcolors.OKGREEN + 'Test 1 Okno rejestracji zostało otworzone poprawnie - PASSED')

try:
    email_field = driver.find_element ('xpath','//*[@id="reg_email"]')
    email_field.send_keys('stanczykadrian3@gmail.com')

    password_field = driver.find_element ('xpath','//*[@id="reg_password"]')
    password_field.submit()

    password_field = driver.find_element ('xpath','//*[@id="reg_password"]')
    password_field.send_keys('testowehaslo')

    register = driver.find_element('xpath','//*[@id="customer_login"]/div[2]/form/p[3]/input[3]')
    register.click()

except:
    print(bcolors.FAIL + 'Test 2 Rejestracja nieudana - FAILED')
    raise
else:
    print(bcolors.OKGREEN + 'Test 2 Rejestracja przebiegła poprawnie - PASSED')
try:
    shop = driver.find_element('xpath','//*[@id="page"]/div/div[1]/div/div/div/span[3]/a/span')
    shop.click()

    scarf = driver.find_element('xpath','//*[@id="page"]/div/div/div[2]/div/ul/li[7]/a/h2')
    scarf.click()

    dod_koszyk = driver.find_element('xpath','//*[@id="page"]/div/div/div[2]/div/ul/li[3]/a[2]')
    dod_koszyk.click()
except:
    print(bcolors.FAIL + 'Test 3 Nie dodano towaru do koszyka - FAILED')
    raise
else:
    print(bcolors.OKGREEN + 'Test 3 Poprawnie dodano towar do koszyka - PASSED')

time.sleep(1)
try:
    koszyk = driver.find_element('xpath','//*[@id="page"]/header[1]/div/div/div/ul/li[2]/a')
    koszyk.click()

    minus_towar = driver.find_element('xpath','//*[@id="post-6"]/div[2]/form/table/tbody/tr[1]/td[5]/div/div/a[1]/span')
    minus_towar.click()

    update_koszyk = driver.find_element('xpath','//*[@id="post-6"]/div[2]/form/table/tbody/tr[2]/td/input[1]')
    update_koszyk.click()

except:
    print(bcolors.FAIL + 'Test 4 Nie usunięto towaru z koszyka - FAILED')
    raise
else:
    print(bcolors.OKGREEN + 'Test 4 Poprawnie usunięto towar z Koszyka - PASSED')


time.sleep(1)
try:
    shop = driver.find_element('xpath','//*[@id="page"]/div/div[1]/div/div/div/span[3]/a/span')
    shop.click()

    jeans = driver.find_element('xpath','//*[@id="page"]/div/div/div[2]/div/ul/li[5]/a/h2')
    jeans.click()

    sortowanie = driver.find_element('xpath','//*[@id="page"]/div/div/div[2]/div/form/select')
    sortowanie.click()

    sortowanie_pop = driver.find_element('xpath','//*[@id="page"]/div/div/div[2]/div/form/select/option[2]')
    sortowanie_pop.click()
except:
    print(bcolors.FAIL + 'Test 5 Towar nie został posortowany - FAILED')
    raise
else:
    print(bcolors.OKGREEN + 'Test 5 Towar został posortowany po popularności - PASSED')

try:
    kup_jeans = driver.find_element('xpath','//*[@id="page"]/div/div/div[2]/div/ul/li[1]/a[2]')
    kup_jeans.click()
    zobacz_koszyk = driver.find_element('xpath','//*[@id="page"]/div/div/div[2]/div/ul/li[2]/a[3]')
except:
    print(bcolors.FAIL + 'Test 6 Koszyk z przycisku View cart nie został otworzony - FAILED')
else:
    print(bcolors.OKGREEN + 'Test 6 Koszyk z przycisku View cart został otworzony- PASSED')
time.sleep(1)

koszyk = driver.find_element('xpath','//*[@id="page"]/header[1]/div/div/div/ul/li[2]/a')
koszyk.click()
try:
    zmiana_ilosci =driver.find_element('xpath',"//*[@class='input-text qty text']").clear()
    zmiana_ilosci = driver.find_element('xpath', "//*[@class='input-text qty text']")
    zmiana_ilosci.click()
    zmiana_ilosci.send_keys('99')
    update_koszyk = driver.find_element('xpath', '//*[@id="post-6"]/div[2]/form/table/tbody/tr[2]/td/input[1]')
    update_koszyk.click()
except:
    print(bcolors.FAIL + 'Test 7 Nie udało się zmienić ilości towaru na 99 - FAILED')
    raise
else:
    print(bcolors.OKGREEN + 'Test 7 Ilość towaru na 99 została zmieniona poprawnie - PASSED')

time.sleep(2)

try:
    zatw_koszyk = driver.find_element('xpath','//*[@id="post-6"]/div[2]/div[2]/div/div/a')
    zatw_koszyk.click()

    first_name = driver.find_element('xpath','//*[@id="billing_first_name"]')
    first_name.click()
    first_name.send_keys('Adrian')

    last_name = driver.find_element('xpath','//*[@id="billing_last_name"]')
    last_name.click()
    last_name.send_keys('Testowy')

    company_name = driver.find_element('xpath','//*[@id="billing_company"]')
    company_name.click()
    company_name.send_keys('Testowy')

    country = driver.find_element('xpath','//*[@id="select2-billing_country-container"]')
    country.click()
    company_name.send_keys(Keys.ARROW_DOWN)
    company_name.send_keys(Keys.ARROW_DOWN)
    company_name.send_keys(Keys.ENTER)

    street = driver.find_element('xpath','//*[@id="billing_address_1"]')
    street.click()
    street.send_keys('Polna 145')

    city = driver.find_element('xpath','//*[@id="billing_city"]')
    city.click()
    city.send_keys('Toruń')

    state = driver.find_element('xpath','//*[@id="billing_state"]')
    state.click()
    state.send_keys('Kujawsko - Pomorskie')

    zip = driver.find_element('xpath','//*[@id="billing_postcode"]')
    zip.click()
    zip.send_keys('87-100')

    phone = driver.find_element('xpath','//*[@id="billing_phone"]')
    phone.click()
    phone.send_keys('333 666 999')
except:
    print(bcolors.FAIL + 'Test 8 Nie udało się uzupełnić formularza zamówienia - FAILED')
    raise
else:
    print(bcolors.OKGREEN + 'Test 8 Formularz zamówienia został poprawnie wypełniony - PASSED')

try:
    payment = driver.find_element('xpath','//*[@id="payment_method_cod"]')

    time.sleep(1)

    payment = driver.find_element('xpath','//*[@id="payment"]/ul/li[3]/label')
    payment.click()

    time.sleep(3)

    order = driver.find_element('xpath','//*[@id="place_order"]')
    order.click()

    time.sleep(5)

    order = driver.find_element('xpath','//*[@id="place_order"]')
except:
    print(bcolors.OKGREEN + 'Test 9 Zamówienie zostało poprawnie złożone - PASSED')
else:
    print(bcolors.FAIL + 'Test 9 Nie udało się złożyć zamówienia - FAILED')


make_screenshot(driver)
driver.close()