import re
import time

import pymysql.cursors
import requests
from bs4 import BeautifulSoup


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def save_db(arr):
    conn = pymysql.connect(host='panalu.ipdisk.co.kr',
                           user='ieye',
                           password='ieye',
                           db='cafe',
                           charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = 'insert into freeboard ( s_title, s_content, s_link, no, cdate ) values( %s, %s, %s, %s, now() ) ON DUPLICATE KEY UPDATE no= %s'
            cursor.executemany(sql, arr)
    finally:
        conn.close()


def goMain(val):
    headers_get = {'Accept-Encoding': None}
    html = requests.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=humor&page=10', headers=headers_get).text
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    arrs = []
    for table_row in soup.select('.list' + val):
        try:
            s_link = "http://www.ppomppu.co.kr/zboard/" + table_row.find(href=re.compile("view.php")).get('href')
            str_no = s_link.split("&")
            s_title = table_row.find("font").text

            if (s_link == '' or str_no == '' or s_title == '.' or s_title == ''): continue

            s_no = str_no[len(str_no) - 1].replace('no=', '')
            html = requests.get(s_link, headers=headers_get).text
            s_content = find_between(html, "<!--DCM_BODY-->", "<!--/DCM_BODY-->")
            print(s_title)
            print(s_link)
            print(s_no)
            # print(s_content)
            val = [s_title, s_content, s_link, s_no, s_no]
            arrs.append(val)
        except ValueError:
            print("error !! ")
    else:
        print("db insert start !!!")
        print(arrs)
        save_db(arrs)


while True:
    print("start server !!!")
    goMain('0')
    goMain('1')
    time.sleep(60 * 15)
