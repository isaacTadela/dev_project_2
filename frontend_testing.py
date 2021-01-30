from selenium import webdriver
from selenium.webdriver.common.by import By

id = 2
chromedriver_path="C:\\Users\Administrator\Desktop\devExp\chromedriver.exe"

try:
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    # opening chrome browser on a desired page
    driver.get(f"http://127.0.0.1:5001/users/get_user_data/{id}")
    print("find_element_by_id = ", driver.find_element_by_id("user").text)
    print("webdriver -", driver.find_element(By.ID, value="user").text)
    driver.close()
except Exception as e:
    raise Exception("test failed")