import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import json
contest_dict = {}

def Read_json():
    with open('./contest.json', 'r',encoding = 'UTF-8-sig') as f:
        json_data = json.load(f)
    print(json_data)


def Parsing(contest_list): # 이름, 주최, 날짜, 접수 여부, D-day
    print("hi")
    print(contest_list)
    #contest_list = contest_text.split('\n')
    contest_dict = {}
    for i in range(0,len(contest_list),5):
        #j = (i // 5) + 1
        contest_dict[contest_list[i]] = dict()
        contest_dict[contest_list[i]]['contest_host'] = contest_list[i+1]
        contest_dict[contest_list[i]]['contest_apply_period'] = contest_list[i+2]
        contest_dict[contest_list[i]]['contest_flag'] = contest_list[i+3]
        if len(contest_list[i+4].split()) == 1:
            contest_dict[contest_list[i]]['contest_D_day'] = contest_list[i+4].split()[0]
            contest_dict[contest_list[i]]['contest_views_count'] = 'NULL'
        else:
            contest_dict[contest_list[i]]['contest_D_day'] = contest_list[i+4].split()[0]
            contest_dict[contest_list[i]]['contest_views_count'] = contest_list[i+4].split()[1]

    with open('contest_ing.json','w', encoding='UTF-8-sig') as make_file: #### write on json file
        json.dump(contest_dict, make_file, ensure_ascii = False, indent = "\t")

def Crawl_To_ThinkU():
    chromedriver = './chromedriver2'
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://thinkyou.co.kr/')    # 크롤링할 사이트 호출

    try:    # 정상 처리

        ##### 접수중 Click
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[3]/div/div[5]/div[1]/a[3]'))
        )    # 해당 태그 존재 여부를 확인하기까지 3초 기다림
        driver.find_element_by_xpath('//*[@id="wrap"]/div[3]/div/div[5]/div[1]/a[3]').click()
        driver.implicitly_wait(10)
        #contest_text = ""
        temp_contest_text = ''
        total_contest_list = []
        for _ in range(8):
            contest_list = driver.find_element_by_xpath('//*[@id="contestArea"]')
            # if temp_contest_text == contest_list.text: # if it crawl to end, break!
            #     print("break")
            #     #print(temp_contest_text)
            #     break
            temp_contest_text = contest_list.text
            total_contest_list.extend(temp_contest_text.split('\n')[1:-1])
            element = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="contestArea"]/div[2]/a[3]'))
            )    # 해당 태그 존재 여부를 확인하기까지 3초 기다림
            element = driver.find_element_by_xpath('//*[@id="contestArea"]/div[2]/a[3]')
            driver.execute_script("arguments[0].click();", element)
            driver.implicitly_wait(5)
            #print(temp_contest_text)
            #print("hi\n\n\n")
        Parsing(total_contest_list)
    except TimeoutException:    # 예외 처리
        print('해당 페이지에 해당 정보가 존재하지 않습니다.')
    finally:
        driver.quit() # 종료driver.quit()


if __name__ == '__main__':
    Crawl_To_ThinkU() 