from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("headless")  # Hide browser window from active screen !

browser = webdriver.Chrome(options=options)
browser.get("https://maktabsharif.ir/karvands")

more_button = browser.find_element(By.CSS_SELECTOR, "body > div > :nth-child(6) > button")
browser.execute_script("arguments[0].click()", more_button)

karvands = browser.find_elements(By.CSS_SELECTOR, "body > div > :nth-child(6) > :nth-child(3) > a")  # document.querySelectorAll()

for karvand in karvands:
    print(karvand.find_element(By.CSS_SELECTOR, 'p').text)
