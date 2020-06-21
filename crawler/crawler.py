import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import json
def Read_json():
    with open('./contest.json', 'r',encoding = 'UTF-8-sig') as f:
        json_data = json.load(f)
        #rint(type(json_data))
    print(json_data)
    #print(json.dumps(json_data))


def Parsing(contest_text): # 이름, 주최, 날짜, 접수 여부, D-day
    contest_list = contest_text.split('\n')
    #print(contest_text)
    #contest_list = contest_list[1:]
    contest_dict = {}
    for i in range(1,len(contest_list)-1,5):
        j = (i // 5) + 1
        contest_dict[contest_list[i]] = dict()
        # print(contest_list[i])
        # print(contest_list[i+1])
        # print(contest_list[i+2])
        # print(contest_list[i+3])
        # print(contest_list[i+4])
        
        #contest_dict[j]['contest_name'] = contest_list[i]
        contest_dict[contest_list[i]]['contest_host'] = contest_list[i+1]
        contest_dict[contest_list[i]]['contest_apply_period'] = contest_list[i+2]
        contest_dict[contest_list[i]]['contest_flag'] = contest_list[i+3]
        if len(contest_list[i+4].split()) == 1:
            contest_dict[contest_list[i]]['contest_D_day'] = contest_list[i+4].split()[0]
            contest_dict[contest_list[i]]['contest_views_count'] = 'NULL'
        else:
            contest_dict[contest_list[i]]['contest_D_day'] = contest_list[i+4].split()[0]
            contest_dict[contest_list[i]]['contest_views_count'] = contest_list[i+4].split()[1]
        # print(contest_name,contest_host,contest_apply_period,contest_flag,contest_D_day)
    Read_json()

    
    #print(json.dumps(contest_dict, ensure_ascii=False, indent = "\t"))
    with open('contest.json','w', encoding='UTF-8-sig') as make_file: #### write on json file
        json.dump(contest_dict, make_file, ensure_ascii = False, indent = "\t")

def Crawl_To_ThinkU():
    chromedriver = './chromedriver2'
    driver = webdriver.Chrome(chromedriver)
    driver.get('https://thinkyou.co.kr/')    # 크롤링할 사이트 호출

    try:    # 정상 처리
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="contestArea"]/div[1]'))
        )    # 해당 태그 존재 여부를 확인하기까지 3초 기다림
        contest_list = driver.find_element_by_xpath('//*[@id="contestArea"]/div[1]')
        #print(contest_list)
        contest_text = contest_list.text
        Parsing(contest_text)

        #soup = BeautifulSoup(contest_list.text, 'html.parser')
        #print(soup.find_all(''))

    except TimeoutException:    # 예외 처리
        print('해당 페이지에 해당 정보가 존재하지 않습니다.')
    finally:
        driver.quit() # 종료driver.quit()

if __name__ == '__main__':
    Crawl_To_ThinkU() 
    ###To do => 수시로 파일을 읽고 추가하는 방식으로 Go