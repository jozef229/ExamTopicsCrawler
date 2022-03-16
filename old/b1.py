# #%%
# import requests
# import random 
# from bs4 import BeautifulSoup

# s = requests.session()
# headers_list = [{ 
# 	'authority': 'httpbin.org', 
# 	'cache-control': 'max-age=0', 
# 	'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"', 
# 	'sec-ch-ua-mobile': '?0', 
# 	'upgrade-insecure-requests': '1', 
# 	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
# 	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
# 	'sec-fetch-site': 'none', 
# 	'sec-fetch-mode': 'navigate', 
# 	'sec-fetch-user': '?1', 
# 	'sec-fetch-dest': 'document', 
# 	'accept-language': 'en-US,en;q=0.9', 
# } # , {...} 
# ] 
# headers = random.choice(headers_list) 

# url = 'https://www.examtopics.com/exams/microsoft/az-204/view/1/'
# print(s.cookies.keys())
# s.cookies.clear()
# r = s.get(url, headers=headers)

# # %%
# soup = BeautifulSoup(r.content, 'html5lib')


# # print(r.content)
# # %%
# print(soup.contents)
# table = soup.find('div', attrs = {'class':'exam-question-card'} )
# # %%
# print(table)
# %%


import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
from selenium.webdriver.common.keys import Keys
import org.openqa.selenium.Keys
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# %%
driver = webdriver.Chrome(ChromeDriverManager().install())
#Specify Search URL 
search_url="https://www.examtopics.com/exams/microsoft/az-204/view/10/" 

# driver.get(search_url.format(q='Car'))
driver.get(search_url)

driver.execute_script("document.body.style.zoom='50%'")

questions = driver.find_elements_by_class_name("card-body")
# .screenshot_as_png 



screenshot_as_bytes = questions[1].screenshot_as_png
with open('c1.png', 'wb') as f:
    f.write(screenshot_as_bytes)

screenshot_as_bytes = questions[2].screenshot_as_png
with open('c2.png', 'wb') as f:
    f.write(screenshot_as_bytes)
# %%


# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--start-maximized')
# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.delete_all_cookies()

driver.get("https://www.examtopics.com/exams/microsoft/az-204/view/9/")
time.sleep(2)

# elem = driver.find_element_by_xpath("//*")
# source_code = elem.get_attribute("outerHTML")
# print(source_code)
try:
    # button = driver.find_element(By.CLASS_NAME, "g-recaptcha")
    driver.find_element(By.CSS_SELECTOR, ".g-recaptcha").click()
    # button.click()
    # print(button)
    print("je to tu spravne")
    # button.send_keys(Keys.RETURN)
except NoSuchElementException as e:
    print("checked")

time.sleep(2)


# elem = driver.find_element_by_xpath("//*")
# source_code = elem.get_attribute("outerHTML")
# print(source_code)

try:

    #the element with longest height on page
    ele=driver.find_element("xpath", '//div[@class="questions-container"]')
    total_height = ele.size["height"]+1000

    driver.set_window_size(1920, total_height)      #the trick
    time.sleep(2)

    # questions = driver.find_elements_by_class_name("card-body")
    # screenshot_as_bytes = questions[1].screenshot_as_png
    # with open('c1.png', 'wb') as f:
    #     f.write(screenshot_as_bytes)
    # screenshot_as_bytes = questions[2].screenshot_as_png
    # with open('c2.png', 'wb') as f:
    #     f.write(screenshot_as_bytes)
except NoSuchElementException as e:
    print("test question")

try:
    errorPage = driver.find_element("xpath", '//img[@src="/assets/images/et/404robot.jpg"]')
    print(len(errorPage))
except NoSuchElementException as e:
    print("all is ok")

driver.quit()

# %%
question-discussion-button


comment-content
close




capcha:
g-recaptcha btn btn-primary





driver.delete_all_cookies()

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
from selenium.webdriver.chrome.service import Service
from io import BytesIO

testName = "az-204"
page = "https://www.examtopics.com/exams/microsoft/az-204/view/"
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('chrome://settings/')
driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.4);')
driver.refresh()



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


def take_screenshot(element, driver, filename='screenshot.png'):
    element.location_once_scrolled_into_view
    size = element.size
    location = element.location
    png = driver.get_screenshot_as_png() # saves screenshot of entire page
    im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
    print(location)
    print(size)
    left = location['x'] / 2
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save(filename) # saves new cropped image
    time.sleep(3)

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
            questions = driver.find_elements(By.CLASS_NAME,"exam-question-card")
            for question in questions:
                print("toto je aktualne", questionNumber)
                time.sleep(2)
                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                questionNumber += 1
                take_screenshot(question, driver, 'exams/' + testName + '/' +  str(questionNumber) + '_question.png')
                question.find_element(By.CSS_SELECTOR, ".question-discussion-button").click()
                time.sleep(5)
                discussion = question.find_element(By.CLASS_NAME, "comments-container ")
                take_screenshot(discussion, driver, 'exams/' + testName + '/' +  str(questionNumber) + '_discussion.png')
                webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                time.sleep(2)
                question.find_element(By.CSS_SELECTOR, ".reveal-solution").click()
                time.sleep(2)
                question.find_element(By.CSS_SELECTOR, ".question-answer").location_once_scrolled_into_view
                take_screenshot(question, driver, 'exams/' + testName + '/' +  str(questionNumber) + '_with_answer.png')
                time.sleep(2)
        except NoSuchElementException as e:
            print("test question")
    else:
        break


driver.quit()
# %%




# import os
# import selenium
# from selenium import webdriver
# import time
# from PIL import Image
# import io
# from selenium.webdriver.common.keys import Keys
# import requests
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import ElementClickInterceptedException
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver import ActionChains
# from PIL import Image

# testName = "az-204"
# page = "https://www.examtopics.com/exams/microsoft/az-204/view/"
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get('chrome://settings/')
# driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.4);')
# driver.refresh()



# def getPage(driver, page, pageNumber):
#     driver.delete_all_cookies()
#     driver.get(page + str(pageNumber) + "/")
#     time.sleep(5)

# def iAmNotRobot(driver):
#     try:
#         driver.find_element(By.CSS_SELECTOR, ".g-recaptcha").click()
#         time.sleep(3)
#         return False
#     except NoSuchElementException as e:
#         return True


# def pageExist(driver):
#     try:
#         driver.find_element("xpath", '//img[@src="/assets/images/et/404robot.jpg"]')
#         return False
#     except NoSuchElementException as e:
#         return True


# # def setSize(driver):
# #     ele=driver.find_element("xpath", '//div[@class="container"]')
# #     total_height = ele.size["height"]+1000
# #     driver.set_window_size(1920, total_height)
# #     time.sleep(4)
    
# from io import BytesIO

# def take_screenshot(element, driver, filename='screenshot.png'):
#     element.location_once_scrolled_into_view
#     size = element.size
#     location = element.location
#     png = driver.get_screenshot_as_png() # saves screenshot of entire page

#     im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
#     print(location)
#     print(size)
#     left = location['x'] / 2
#     top = location['y']
#     right = location['x'] + size['width']
#     bottom = location['y'] + size['height']


#     im = im.crop((left, top, right, bottom)) # defines crop points
#     im.save(filename) # saves new cropped image

# pageNumber = 0
# questionNumber = 0
# getPage(driver, page, pageNumber)
# os.makedirs('exams/' + testName, exist_ok=True)
# while True:
#     pageNumber += 1
#     getPage(driver, page, pageNumber)
#     iAmNotRobot(driver)
#     if pageExist(driver) and iAmNotRobot(driver):
#         try:
#             questions = driver.find_elements_by_class_name("exam-question-card")
#             for question in questions:
#                 time.sleep(2)
#                 webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#                 question.location_once_scrolled_into_view
#                 take_screenshot(question, driver)
#                 print("///////////////")
#                 print(questionNumber)
#                 questionNumber += 1
#                 screenshot_as_bytes = question.screenshot_as_png
#                 with open('exams/' + testName + '/' +  str(questionNumber) + '_question.png', 'wb') as f:
#                     f.write(screenshot_as_bytes)
#                 # question.screenshot("asdasd.png")

#                 time.sleep(2)
#                 question.find_element(By.CSS_SELECTOR, ".question-discussion-button").click()
#                 time.sleep(10)
#                 # setSize(driver)
#                 discussion = driver.find_element_by_class_name("comments-container ")
#                 screenshot_as_bytes = discussion.screenshot_as_png
#                 with open('exams/' + testName + '/' +  str(questionNumber) + '_discussion.png', 'wb') as f:
#                     f.write(screenshot_as_bytes)
#                 webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

#                 time.sleep(2)
#                 question.find_element(By.CSS_SELECTOR, ".reveal-solution").click()
#                 time.sleep(2)
#                 question.find_element(By.CSS_SELECTOR, ".question-answer").location_once_scrolled_into_view
#                 time.sleep(2)
#                 # setSize(driver)
#                 screenshot_as_bytes = question.screenshot_as_png
#                 with open('exams/' + testName + '/' +  str(questionNumber) + '_with_answer.png', 'wb') as f:
#                     f.write(screenshot_as_bytes)
#                 time.sleep(2)
                
#         except NoSuchElementException as e:
#             print("test question")
#     else:
#         break


# driver.quit()