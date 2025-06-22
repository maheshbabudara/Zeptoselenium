from selenium.common import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains,Keys
from time import sleep


class Base:
    def __init__(self,driver):
        self.driver=driver
        self.action=ActionChains(self.driver)

    def search_element(self,locator):
        # element=self.driver.find_element(*locator)
        # return element
        element=WebDriverWait(self.driver,10,poll_frequency=0.5,ignored_exceptions=[NoSuchElementException,
                                                                                    ElementNotSelectableException,
                                                                    ElementNotVisibleException,Exception]).until(
            e.presence_of_element_located(locator)
        )
        return element
    def search_elements(self,locator):
        elements=self.driver.find_elements(*locator)
        return elements
    def click_method(self,locator):
        click_action=self.search_element(locator)
        click_action.click()
    def send_data(self,locator,data):
        add_data=self.search_element(locator)
        add_data.send_keys(data)
    def list_boxes(self,locator):
        list=Select(self.search_element(locator))
        list.select_by_value('value')
        list.select_by_index(2)
        list.select_by_visible_text('mahesh')
        list.deselect_all()
        list.deselect_by_index(3)
        list.deselect_by_value('value')
        list.deselect_by_visible_text('rony')
        values=list.options
        for item in values:
            if item.text=='rony mahesh':
                item.click()
                break
    def Action(self,locator):
        web_element=self.search_element(locator)
        self.action.move_to_element(web_element).perform()
        self.action.context_click(web_element).perform()
        self.action.double_click(web_element).perform()
        self.action.click_and_hold(web_element).release(web_element).perform()
        self.action.drag_and_drop(web_element,web_element).perform()
        self.action.move_by_offset(100,300).perform()
        self.action.key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).perform()
        self.action.send_keys(Keys.TAB).perform()
        self.action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        self.action.scroll_to_element(web_element).perform()
        self.action.scroll_by_amount(300,0).perform()
    def popups(self,data):
        pop=self.driver.switch_to.alert
        pop.accept()
        pop.dismiss()
        pop.send_keys(data)
    def frames(self,locator):
        webelement=self.search_element(locator)
        self.driver.switch_to.frame('id')
        self.driver.switch_to.frame('name')






