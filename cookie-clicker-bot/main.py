from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

def store():
    # Target all store elements
    store = driver.find_elements(By.CSS_SELECTOR, "#store div")
    # Run through all store elements backwards
    # The exception allows it to skip items that aren't currently clickable
    for i in range(len(store), -1, -1):
        try:
            store[i].click()
        except:
            continue

cookie = driver.find_element(By.ID, "cookie")

# Run indefinitely
while True:
    # Click 100 times per second for 5 seconds, originally used time.sleep(0.01) but it's unnecessary
    for i in range(0, 500):
        cookie.click()

    # After 5 seconds click every item in the store in reverse 5 times
    # This helps in the early game where you can often do multiple upgrades per 5 second increment
    for i in range(0, 5):
        store()