from Base import basecode
from Pages.pageobjmodel import modelcall
import pytest
from datagenerator.genrtdata import datadrivens

@pytest.mark.parametrize("data",datadrivens())
def test_method1(data):
    driver=basecode.drvopen()
    driver.maximize_window()
    md=modelcall(driver)
    md.enter_username(data[0])
    md.enter_email(data[1])
