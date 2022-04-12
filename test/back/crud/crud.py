import pymysql
import sys

conn = None
cur = None

try:
    conn = pymysql.connect(user="tester", password="mcmong12", host="127.0.0.1", database= "test", port=3306)
        
    # db select, insert, update, delete 작업 객체
    cursor = conn.cursor()
    # # 실행할 select 문 구성
    select_where_query = "SELECT * from solardata WHERE data_id = %s" 

    data_id = 4

    cursor.execute(select_where_query,(data_id))
    # cursor.execute(select_where_query)
    resultset = cursor.fetchall()

    print(resultset)
    # for data_id, phase in resultset: 
    #     print(f"data_id: {data_id}, phase: {phase}")

    # sql = "SELECT * FROM tbl ORDER BY 1 DESC"
    # cursor 객체를 이용해서 수행한다.
    # cursor.execute(sql)
    # # select 된 결과 셋 얻어오기
    # resultList = cursor.fetchall()  # tuple 이 들어있는 list
    # print(resultList)
    # # DB 에 저장된 rows 출력해보기

    # for result in resultList:
    #     seq = result[0]  # seq
    #     title = result[1]  # title
    #     content = result[2]  # content
    #     info = "seq:{}, title :{}, content :{}".format(seq, title, content)

    #     print(info)

except pymysql.Error as err:

    print(err)