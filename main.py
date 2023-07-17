from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# from selenium.webdriver.firefox.options import Options
# options = Options()
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# driver = webdriver.Firefox(options=options)

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
# driver = webdriver.Edge()
driver.get('https://klik-test.ru/')
elem1 = driver.find_element(By.ID, 'clicker')

cps = []
while True:
    while True:
        try:
            elem1.click()
        except:
            break
    time.sleep(1)
    elem2 = driver.find_element(By.ID, 'result-info')
    print(elem2.text)
    cps.append(int(elem2.text.split()[0]))
    print('Средний КПС = ', sum(cps) / len(cps) / 10)

    elem2 = driver.find_element(By.ID, 'modal-ok')
    elem2.click()

    elem2 = driver.find_element(By.ID, 'reset')
    elem2.click()


time.sleep(3)
driver.close()