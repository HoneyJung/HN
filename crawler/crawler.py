import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

chromedriver = './chromedriver2'
driver = webdriver.Chrome(chromedriver)
driver.get('https://thinkyou.co.kr/')    # 크롤링할 사이트 호출

#print(driver.find_element_by_xpath('//*[@id="contestArea"]/div[1]'))

try:    # 정상 처리
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="contestArea"]/div[1]'))
    )    # 해당 태그 존재 여부를 확인하기까지 3초 기다림
    contest_list = driver.find_element_by_xpath('//*[@id="contestArea"]/div[1]')
    print(contest_list.text)
except TimeoutException:    # 예외 처리
    print('해당 페이지에 해당 정보가 존재하지 않습니다.')
finally:
    driver.quit() # 종료driver.quit()