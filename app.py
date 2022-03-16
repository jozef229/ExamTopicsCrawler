#%%
import os
import selenium
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
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from io import BytesIO
import lxml

testName = "az-204"
page = "https://www.examtopics.com/exams/microsoft/az-204/view/"
proxy_page = 'https://proxyscrape.com/web-proxy'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def getPage(driver, proxy_page, page, pageNumber):
    driver.delete_all_cookies()
    driver.get(proxy_page)
    input = driver.find_element(By.CLASS_NAME, "form-control")
    input.clear()
    time.sleep(2)
    input.send_keys(page + str(pageNumber) + "/")
    driver.find_element(By.CSS_SELECTOR, ".btn").click()
    time.sleep(12)


def iAmNotRobot(driver):
    try:
        driver.find_element(By.CSS_SELECTOR, ".g-recaptcha").click()
        time.sleep(7)
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
# getPage(driver, proxy_page, page, pageNumber)
os.makedirs('exams/' + testName, exist_ok=True)
while True:
    pageNumber += 1
    getPage(driver, proxy_page, page, pageNumber)
    iAmNotRobot(driver)
    if pageExist(driver) and iAmNotRobot(driver):
        try:
            soup=BeautifulSoup(driver.page_source, 'lxml')
            questions_soup = soup.select('.exam-question-card')
            questions_selenium = driver.find_elements(By.CLASS_NAME, "exam-question-card")
            for index in range( len(questions_selenium) ):
                questionNumber += 1
                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                question_html = str(questions_soup[index]).replace("src=\"/assets", "src=\"https://www.examtopics.com/assets").replace("  ", "")
                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                unique = list(dict.fromkeys(questions_soup[index].find_all(attrs={"data-id": True})))
                discussion = []
                for item in questions_soup[index].find_all(attrs={"data-id": True}):
                    discussion.append(item['data-id'])
                discussion = list(set(discussion))
                time.sleep(2)
                decission_page = requests.get( "https://www.examtopics.com/ajax/discussion/exam-question/" + discussion[0] + "/")
                decission_soup = BeautifulSoup(decission_page.text, 'html.parser')
                decission_html = str(decission_soup)
                text_file_decission = open('exams/' + testName + '/' +  str(questionNumber) + '_discussion.html', "w")
                text_file_decission.write(decission_html)
                text_file_question = open('exams/' + testName + '/' +  str(questionNumber) + '_question.html', "w")
                text_file_question.write(question_html)
                time.sleep(5)
        except NoSuchElementException as e:
            print("test question")
    else:
        break


driver.quit()
# %%
