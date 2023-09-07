from Library import readconfig
from selenium.webdriver.support.select import Select
from Library import readconfig

class modelcall():

    def __init__(self,obj):
        global driver
        driver=obj
    def enter_username(self,username):
        driver.find_element('name', readconfig.elements("Locators", "usr_name")).send_keys(username)
    def enter_email(self,email):
        driver.find_element('name', readconfig.elements("Locators", "email_name")).send_keys(email)

    def address_type(self,address):
        driver.find_element('xpath', f"//input[@value='{address}']").click()

    def enter_sex(self,sex):
        slt = Select(driver.find_element('name', readconfig.elements("Locators", "sex_name")))
        slt.select_by_visible_text(sex)