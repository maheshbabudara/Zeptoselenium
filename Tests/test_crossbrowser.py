from time import sleep

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


#working fine with Hardcoded Values:
# browser = 'firefox'  # chnage it
# sleep(5)
# def test_check():
#     global driver
#     if browser == 'chrome':
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif browser == "edge":
#         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     elif browser == 'firefox':
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     else:
#         print('No browser Name')
#
#     driver.get('https://www.youtube.com/')
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     sleep(2)
#     print("Title:", driver.title)
#     assert driver.title == 'YouTube'
#     driver.close()

#COMMANDS TO EXECUTE ABOVE SCRIPTS:
# CMD: pytest filename




# *********************************SCRIPT IS CORRECT BUT EXECUTEING:*****************************************
# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
#

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome, edge, firefox")
#
# @pytest.fixture
# def driver(request):
#     browser = request.config.getoption("--browser")
#     if browser == "chrome":
#         driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     elif browser == "edge":
#         driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     elif browser == "firefox":
#         driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     else:
#         raise ValueError('No valid browser provided')
#
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
#COMMANDS TO EXECUTE BY COMMAND LINE OPTIONS:
# CMD: pytest filename --browser=firefox  # Replace 'firefox' with 'chrome' or 'edge' as needed






#*******************USING ENVIROMENT VARIABLES by importing OS:  *******************WORKING FINE*********
import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture
def driver(request):
    browser = os.getenv("BROWSER", "chrome")  # Default to Chrome if not set
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError('No valid browser provided')

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_check(driver):
    driver.get('https://www.youtube.com/')
    print("Title:", driver.title)
    assert driver.title == 'YouTube'

#COMMANDS TO EXECUTE BY ENVIROMENT SETUP:
# STEP1: set BROWSER=chrome
# STEP2: pytest filename
