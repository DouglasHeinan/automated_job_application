from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import ElementClickInterceptedException
# from selenium.common.exceptions import StaleElementReferenceException
import time
import os

PASSWORD = os.environ["PASSWORD"]
USERNAME = os.environ["USERNAME"]
PHONE_NUM = os.environ["PHONE_NUM"]
WEBPAGE = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101758306&keywords=python%20developer&sortBy=R"


def main():

    service = Service(r"C:\Users\dough\OneDrive\Documents\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get(WEBPAGE)

    sign_in_btn = driver.find_element(By.CSS_SELECTOR, ".nav__cta-container .nav__button-secondary")
    sign_in_btn.click()
    time.sleep(1)
    username = driver.find_element(By.ID, "username")
    username.send_keys(USERNAME)
    password = driver.find_element(By.ID, "password")
    password.send_keys(PASSWORD)
    form_sign_in_btn = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container .from__button--floating")
    form_sign_in_btn.click()
    time.sleep(2)
    apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
    apply_btn.click()
    time.sleep(2)
    phone_number = driver.find_element(By.CSS_SELECTOR, ".fb-single-line-text input")
    if phone_number.text == "":
        phone_number.send_keys(PHONE_NUM)
    confirm_btn = driver.find_element(By.CSS_SELECTOR, ".pv4 button")
    confirm_btn.click()

    time.sleep(200)


if __name__ == '__main__':
    main()
