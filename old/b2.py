
# %%
import os
import selenium
from io import BytesIO
from selenium import webdriver
import time
from PIL import Image
import io
from selenium.webdriver.common.keys import Keys
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from PIL import Image

testName = "az-204"
page = "https://www.examtopics.com/exams/microsoft/az-204/view/"
driver = webdriver.Chrome(ChromeDriverManager().install())


def getPage(driver, page, pageNumber):
    driver.delete_all_cookies()
    driver.get(page + str(pageNumber) + "/")
    time.sleep(5)

def iAmNotRobot(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, ".g-recaptcha").click()
        time.sleep(3)
        return False
    except NoSuchElementException as e:
        return True


def pageExist(driver):
    try:
        driver.find_element("xpath", '//img[@src="/assets/images/et/404robot.jpg"]')
        return False
    except NoSuchElementException as e:
        return True


pageNumber = 0
questionNumber = 0
getPage(driver, page, pageNumber)
os.makedirs('exams/' + testName, exist_ok=True)
while True:
    pageNumber += 1
    getPage(driver, page, pageNumber)
    iAmNotRobot(driver)
    if pageExist(driver) and iAmNotRobot(driver):
        try:
            questions = driver.find_elements_by_class_name("exam-question-card")
            for question in questions:
                source_code = question.get_attribute("outerHTML")
                # print(source_code)
                with open('exams/' + testName + '/' +  str(questionNumber) + '_with_answer.txt', 'wb', encoding='utf-8') as f:
                    f.write(source_code)
                
        except NoSuchElementException as e:
            print("test question")
    else:
        break


driver.quit()
# %%
