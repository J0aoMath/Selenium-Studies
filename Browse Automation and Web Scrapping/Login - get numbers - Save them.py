from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime as dt

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features = AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/login/")
    return driver

def write_file(text):
    filename = f'{dt.now().strftime("%Y%m%d%H%M%S")}.txt'
    with open(filename, 'w') as file:
        file.write(text)

def get_number(s):
    ss = str(s).split(':')
    print(ss)
    return float(ss[1])

def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys('automated')
    sleep(1)
    driver.find_element(by="id", value="id_password").send_keys('automatedautomated'+ Keys.RETURN)
    sleep(1)
    driver.find_element(by='xpath', value='/html/body/nav/div/a').click()
    sleep(1.5)
    while True:
        sleep(4)
        element = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]') 
        write_file(str(get_number(element.text))) 

main()
