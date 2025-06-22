import allure
from allure_commons.types import AttachmentType

from POM.practisefile import practise
from time import sleep



def test_country_web(country):
    c = practise(country)
    c.prac()
    condition = country.find_element("xpath", "//strong[text()='Egypt']").is_displayed()
    if condition == False:
        allure.attach(country.get_screenshot_as_png(), name='test_country_web.png', attachment_type=AttachmentType.PNG)
    assert condition

# import allure
# import pytest
# from allure_commons.types import AttachmentType
#
# from POM.Blog_practise import utube
# from time import sleep
#
# @pytest.mark.utube
# def test_youtube(u):
#     d = utube(u)
#     d.tube('king of Kotha')
#     condition = u.find_element('xpath',
#                                '//h3[@class="title-and-badge style-scope ytd-video-renderer"]/a[@title="People of Kotha Motion Poster | King of Kotha | Dulquer Salmaan | Abhilash Joshiy | Jakes Bejoy"]').is_displayed()
#     if condition == True:
#         allure.attach(u.get_screenshot_as_png(), name='bug_screenshot.png', attachment_type=AttachmentType.PNG)
#     assert condition
