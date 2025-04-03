from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

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

def get_number(s):
    s = s.split(':')
    return s[1]

def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys('automated')
    sleep(1)
    driver.find_element(by="id", value="id_password").send_keys('automatedautomated'+ Keys.RETURN)
    sleep(1)
    driver.find_element(by='xpath', value='/html/body/nav/div/a').click()
    sleep(1.5)
    while True:
        element = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]')
        print(element.text)
        print(get_number(element.text))
        sleep(2)

        
