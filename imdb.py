from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# driver.get('https://www.imdb.com/chart/top/')
# spisok = driver.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')
# for s in spisok:
#     title = s.find_element(By.CLASS_NAME, 'ipc-title__text')
#     rating = s.find_element(By.CLASS_NAME, 'ipc-rating-star')
#     print(title.text, rating.text)
#     if float(rating.text) < 9:
#         break
# time.sleep(3)
# driver.close()


driver.get('https://www.imdb.com/chart/toptv/')
spisok = driver.find_elements(By.CLASS_NAME, 'ipc-metadata-list-summary-item')
for s in spisok:
    title = s.find_element(By.CLASS_NAME, 'ipc-title__text')
    if int(title.text.split('.')[0]) <= 10:
        print(title.text)

print('########################################')
for s in spisok:
    title = s.find_element(By.CLASS_NAME, 'ipc-title__text')
    year = s.find_element(By.CLASS_NAME, 'cli-title-metadata-item')
    if '2016' in year.text:
        print(title.text, year.text)
