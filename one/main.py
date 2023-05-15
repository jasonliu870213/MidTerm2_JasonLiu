from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import pandas as pd
data = pd.read_excel('PHPTravels-TestCases.xlsx')

def wait_for(path):
    try:
        return wait.until(EC.visibility_of_element_located((By.XPATH, path)))
    except TimeoutException:
        print('get element fail')
        return None

def click_element(path):
    try:
        element = wait_for(path)
        element.click()
    except Exception as e:
        print('Click', path, 'FAIL')
        #print(e)


def input_value(path,value):
    try:
        element = wait_for(path)
        element.clear()
        element.send_keys(value)
    except Exception as e:
        print(path, 'FAIL')
        print(e)

def check_element(path):
    try:
        element = wait_for(path)
        return 'success'
    except Exception as e:
        #print(e)
        return 'failed'


for index, row in data.iterrows():
    testcase = 1
    email = row.Email
    password = row.Password
    result = row.Result
    print(email, password)
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)  # Set wait time
    driver.maximize_window()
    driver.get('https://phptravels.net/admin') #in
    input_value("//div[@class='mb-2']//input[@name='email']", email)
    input_value("//div[@class='mb-2']//input[@name='password']", password)
    click_element("//button[@type='submit']")
    if check_element("//button[@id='dropdownMenuProfile']") == result:
        print(f'Test Case {testcase} Success!')
    else:
        print(f'Test Case {testcase} Failed!')
    testcase += 1
    driver.quit()

