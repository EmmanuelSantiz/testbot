from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def Login():
    print('method: Login')
    browser.find_element_by_xpath('//*[@id="login-link"]').click()
    time.sleep(2)
    print('----- Write Form')
    browser.find_element_by_xpath('//*[@id="email"]').send_keys("bottest@emmanuel.com")
    browser.find_element_by_xpath('//*[@id="pass"]').send_keys("bottes01")
    time.sleep(2)
    try:
        print('----- Click: Send Form!')
        browser.find_element_by_xpath('//*[@id="send2"]').click()
        bandera = True
    except NoSuchElementException:
        bandera = False
    return bandera

def checkout():
    print('method: Chekcout')
    try:
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[2]/a').click()
        bandera = True
    except NoSuchElementException:
        bandera = False
    return bandera

def cart():
    print('method: Cart')
    try:
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/main/div[2]/div/div[1]/div/a').click()
        bandera = True
    except NoSuchElementException:
        bandera = False
    time.sleep(2)
    if bandera:
        addItem()
    else:
        goPayment()
        time.sleep(5)
        isShipping()

def goPayment():
    print('method: goPayment')
    try:
        time.sleep(2)
        browser.find_element_by_xpath('/html/body/div[3]/main/div[2]/div/div[1]/div/div[2]/form/div[1]/div[4]/button').click()
    except NoSuchElementException:
        print('Aca no hay nada')

def isShipping():
    typeDelivery = browser.find_element_by_id('curb_type')
    if typeDelivery.text == 'PICK&GO':
        typeDelivery.click()
        #elegir direccion
    else:
        print('revisar horarios')

def addItem():
    print('method: addItem')
    time.sleep(2)
    categorias = ['//*[@id="ui-id-2"]', '//*[@id="ui-id-3"]','//*[@id="ui-id-4"]']
    print('----- Go to Category')
    browser.find_element_by_xpath(categorias[1]).click()
    time.sleep(2)
    print('----- Button link product')
    browser.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div[7]/ol/li[1]/div[2]/a').click()
    time.sleep(2)
    print('----- Button add cart')
    browser.find_element_by_xpath('/html/body/div[2]/main/div[1]/div/div/div[2]/div/div[2]/div[4]/div[1]/form/div/button').click()
    time.sleep(3)
    cart()

def error():
    print('algo salio mal')

opt = int(input("Elige Opcion\n 1.- Revisar Horarios\n2.-Test \n3.- Salir"))

browser = webdriver.Firefox()

print('###########################################')
print('Run URL: https://dev.hebdigital.net')

browser.get('https://dev.hebdigital.net')
time.sleep(5)

if Login():
    print('Login Success')
    time.sleep(2)
    if checkout():
        time.sleep(2)
        cart()
    else:
        print('checkout error')
        error()
else:
    print('login error')
    error()

#browser.find_element_by_xpath('//*[@id="curb_type"]').click() revisar checkout