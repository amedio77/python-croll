# -*- coding: utf-8 -*-

import requests
import pymysql.cursors
from bs4 import BeautifulSoup

print( '한글' )

# HTTP GET Request
req = requests.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=humor&page=10')

req.raise_for_status()

print(req.encoding)

req.encoding = 'utf-8'

html = req.text


print(html)


#soup = BeautifulSoup(html, 'html.parser')

#print(soup)


'''
conn = pymysql.connect(host='panalu.ipdisk.co.kr',
                       user='ieye',
                       password='',
                       db='blog',
                       charset='utf8')

try:
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM user WHERE pw = %s'
        cursor.execute(sql, ('1234',))

        result = cursor.fetchone()
        print(result)
        # (1, 'test@test.com', 'my-passwd')
finally:
    conn.close()
'''
