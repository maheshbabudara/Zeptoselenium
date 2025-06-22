import allure
import pytest
from allure_commons.types import AttachmentType
from POM.demo_login import login
from Utilities.Excelreader import reader

cred_details = reader('Test_data.xlsx', 'login')


@pytest.mark.login
@pytest.mark.parametrize('username,password', cred_details)
def test_demo_login(demo,username, password):
    l = login(demo)
    l.log(username, password)
    condition = demo.find_element("link text", "Log out").is_displayed()
    print(condition)
    if condition == False:
        allure.attach(demo.get_screenshot_as_png(), name="test_demo_login.png", attachment_type=AttachmentType.PNG)
    assert condition
