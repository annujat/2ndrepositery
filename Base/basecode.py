from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver import firefox
from Library import readconfig


def drvopen():
    global driver
    if readconfig.configs("Details","browser")=="chrome":
        drivpath="./Driver/chromedriver.exe"
        service=chrome.service.Service(executable_path=drivpath)
        option=webdriver.ChromeOptions()
        driver=webdriver.Chrome(service=service,options=option)
        driver.get(readconfig.configs("Details","app_url"))
    elif readconfig.configs("Details","browser")=="firefox":
        drivpath="./Driver/geckodriver.exe"
        servi=firefox.service.Service(executable_path=drivpath)
        option=webdriver.FirefoxOptions()
        option.binary_location="C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        driver=webdriver.Firefox(service=servi,options=option)
        driver.get(readconfig.configs("Details", "app_url"))
    return driver

def drvclose():
    driver.close()