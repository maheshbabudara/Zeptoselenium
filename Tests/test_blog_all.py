# # import pytest
# # from POM.Blog_practise import Blog_practise
# # from time import sleep
# #
# #
# # @pytest.mark.practise
# # def test_blog(b):
# #     bl=Blog_practise(b)
# #     bl.practise("Mahesh",'rony@gmail.com')
# import allure
# import pytest
# from allure_commons.types import AttachmentType
#
# from POM.Blog_practise import Blog_practise
# from time import sleep


import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains, Keys
from time import sleep


import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(autouse=True)
def setup(browser, request):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(service=GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeChromiumDriverManager().install())

    driver.get("https://www.google.com/search?gs_ssp=eJzj4tTP1TcwLzFNMjZg9OLOTcxILc5QSEpMKgUAUwYHOg&q=mahesh+babu&oq=mahesh&gs_lcrp=EgZjaHJvbWUqDAgBEC4YJxiABBiKBTIPCAAQIxgnGOMCGIAEGIoFMgwIARAuGCcYgAQYigUyBggCEEUYOTIPCAMQLhhDGLEDGIAEGIoFMg8IBBAAGEMYsQMYgAQYigUyBggFEEUYPDIGCAYQRRg8MgYIBxBFGDzSAQgyMDY3ajBqN6gCCLACAQ&sourceid=chrome&ie=UTF-8")
    driver.maximize_window()
    request.cls.driver = driver

    yield driver  # This will allow the test to run

    driver.quit()  # Ensure the driver quits after the tests

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, edge")

@pytest.fixture(scope='class', autouse=True)
def browser(request):
    return request.config.getoption("--browser")
