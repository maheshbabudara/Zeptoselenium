import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os
# location=os.getcwd()


@pytest.fixture()
def demo():
    demo=WebDriver()
    option=Options()
    option.add_argument("--disable-Notifications")
    option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    option.add_experimental_option("detach",True)
    preferences={"download.default_directory":location,"always.open_pdf_externally":True}
    option.add_experimental_option("prefs",preferences)
    demo.get("https://demowebshop.tricentis.com/")
    demo.implicitly_wait(10)
    demo.maximize_window()
    yield demo
    demo.close()

@pytest.fixture()
def tes():
    tes=WebDriver()
    option=Options()
    tes.get("https://testautomationpractice.blogspot.com/")
    tes.implicitly_wait(10)
    tes.maximize_window()
    yield tes
    # tes.close()


# @pytest.fixture()
# def b():
#     b=WebDriver()
#     option=Options()
#     b.get("https://testautomationpractice.blogspot.com/")
#     b.maximize_window()
#     b.implicitly_wait(10)
#     yield b
#     b.close()
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
location = os.getcwd()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def b():
    location = "/tmp/downloads"  # Or any valid path you want

    options = Options()
    driver = WebDriver()
    preferences = {
        "download.default_directory": location,
        "plugins.always_open_pdf_externally": True
    }
    options.add_experimental_option("prefs", preferences)
    options.add_experimental_option("detach", True)

    # Headless + CI-safe options
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # Create driver with options
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()



# location = os.getcwd()

@pytest.fixture()
def zepto():
    zepto = WebDriver()
    option = Options()
    option.add_argument("--disable-notifications")
    option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    option.add_experimental_option("detach", True)
    preferences = {"download.default_directory": location, 'plugins.always_open_pdf_externally': True}
    option.add_experimental_option('prefs', preferences)
    zepto.get("facebook")
    zepto.implicitly_wait(10)
    zepto.maximize_window()

    yield zepto
    zepto.close()

@pytest.fixture()
def u():
    u=WebDriver()
    option=Options()
    option.add_argument('--disable-notifications')
    # option.add_argument('--headless')
    # option.add_argument('--disable-gpu')
    option.add_experimental_option('detach',True)
    preferences={'download.default_directory':location,'plugins.always_open_pdf_externally':True}
    option.add_experimental_option('prefs',preferences)
    u.get('https://www.youtube.com/')
    u.implicitly_wait(10)
    u.maximize_window()
    yield u
    u.close()




import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def country(request):
    # Determine browser from environment variable or default to Chrome
    browser_name = os.getenv('BROWSER', 'chrome')
    # Browser options setup
    options = Options()
    options.add_argument('--disable-notifications')
    # options.add_argument('--headless')  # Run browser in headless mode
    # options.add_argument('--disable-gpu')
    options.add_experimental_option('detach', True)

    # Download directory preferences, replace with actual location
    location = '/path/to/downloads'  # Make sure this is a valid path
    preferences = {
        'download.default_directory': location,
        'plugins.always_open_pdf_externally': True
    }
    options.add_experimental_option('prefs', preferences)

    # Initialize WebDriver based on selected browser
    if browser_name == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
    elif browser_name == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    else:
        raise ValueError(f'No such browser: {browser_name}')

    # Open the URL and maximize window
    driver.get("https://cosmocode.io/automation-practice-webtable/")
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Yield driver to the test
    yield driver

    # Cleanup after the test
    driver.quit()


