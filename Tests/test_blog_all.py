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

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture(scope="class", autouse=True)
def setup(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise Exception(f"Unsupported browser: {browser}")

    driver.maximize_window()
    driver.get("https://www.google.com")

    request.cls.driver = driver
    yield
    driver.quit()

# Hook to add command-line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests with: chrome/firefox/edge"
    )

# Fixture to return browser value from CLI
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, firefox, edge")

@pytest.fixture(scope='class', autouse=True)
def browser(request):
    return request.config.getoption("--browser")
