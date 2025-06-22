from Lib.library import Base
from time import sleep
from Utilities.Locator import demo_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e

class login(Base):
    def log(self,un,pwd):
        self.click(demo_locators.login)
        sleep(1)
        web_element=WebDriverWait(self.driver,10).until(
            e.presence_of_element_located((demo_locators.username_text))
        )
        web_element.send_keys(un)
        sleep(1)
        self.send_data(demo_locators.password_text,pwd)
        sleep(1)
        self.click(demo_locators.submit_btn)
        sleep(2)



