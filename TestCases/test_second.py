from Base import basecode
from Pages.pageobjmodel import modelcall
import time
from Library import readconfig
def test_secmethod():
    driver=basecode.drvopen()
    md=modelcall(driver)
    md.address_type("home")
    md.enter_sex("Male")
    time.sleep(5)
    cls=basecode.drvclose()

