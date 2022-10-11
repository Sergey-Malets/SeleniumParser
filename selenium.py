
from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome() #запускаем драйвер
browser.get("http://hh.ru")

search_input = browser.find_element(By.ID, "a11y-search-input")
search_input.send_keys("Junior Python")

search_button = browser.find_element(By.CSS_SELECTOR, "[data-qa='search-button']")
search_button.click()

job_count = browser.find_element(By.CSS_SELECTOR, "[data-qa='vacancies-search-header'] h1") #заголовок с ко-вом ваканий
print(job_count.text)

# time.sleep(300)
import re
count = re.sub(r"\D","",job_count.text)
print(count)

browser.close()