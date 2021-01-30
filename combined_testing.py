import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By

id = 19971231
user_name = "my Name"

chromedriver_path="C:\\Users\Administrator\Desktop\devExp\chromedriver.exe"

try:
    res = requests.post(f'http://127.0.0.1:5000/users/{id}', json={"user_name": f'{user_name}'})
    print("post -", res.json())

    res = requests.get(f'http://127.0.0.1:5000/users/{id}')
    print("get -", res.json())

    host, port, user, passwd, db = 'remotemysql.com', 3306, '9hkyb0ebUg', 'Q9XsNQ9fQw', '9hkyb0ebUg'
    # Establishing a connection to DB
    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, cursorclass=pymysql.cursors.DictCursor)
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM 9hkyb0ebUg.users WHERE user_id = {id};")
    data = cursor.fetchall()
    user_name = data[0]['user_name']
    print("DB -", user_name)

    # driver = webdriver.Chrome(executable_path=chromedriver_path)
    # # opening chrome browser on a desired page
    # driver.get(f"http://127.0.0.1:5001/users/get_user_data/{id}")
    # name = driver.find_element(By.ID, value="user").text
    # print("webdriver -", name)

except Exception as e:
    raise Exception("test failed")