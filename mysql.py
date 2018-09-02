import pymysql.cursors

conn = pymysql.connect(host='amedio0222.cafe24.com',
                       user='amedio0222',
                       password='lw11090725!',
                       db='amedio0222',
                       charset='utf8')

try:
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM freeboard WHERE seq = %s'
        cursor.execute(sql, ('1',))
        result = cursor.fetchone()
        print(result)
        # (1, 'test@test.com', 'my-passwd')
finally:
    conn.close()
