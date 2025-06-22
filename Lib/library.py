# from time import sleep
# from selenium import webdriver
# from selenium.common import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as e
# from selenium.webdriver import ActionChains, Keys
#
#
# class Base:
#     def __init__(self, driver):
#         self.driver = driver
#         self.action = ActionChains(self.driver)
#
#     def search_element(self, locator):
#         element = self.driver.find_element(*locator)
#         return element
#
#     def search_elements(self, locator):
#         elements = self.driver.find_elements(*locator)
#         return elements
#
#     def click(self, locator):
#         item = self.search_element(locator)
#         item.click()
#
#     def click_multi(self, locator):
#         items = WebDriverWait(self.driver, 10,
#                               ignored_exceptions=[NoSuchElementException, ElementNotSelectableException,
#                                                   ElementNotVisibleException, Exception], poll_frequency=0.3).until(
#             e.visibility_of_all_elements_located(locator)
#         )
#         # items=self.search_elements(locator)
#         for i in items:
#             if i.text == 'monday' or i.text == "sunday" or i.text == 'Thursday':
#                 i.click()
#
#     def send_data(self, locator, data):
#         item = self.search_element(locator)
#         item.send_keys(data)
#
#     def drop(self, locator):
#         item = Select(self.search_element(locator))
#         item.select_by_index(3)
#         item.select_by_value('value')
#         item.select_by_visible_text('text')
#         item.deselect_all()
#         item.deselect_by_index(3)
#         item.deselect_by_value('value')
#         item.deselect_by_visible_text('text')
#         opt = item.options
#         for v in opt:
#             if v.text == "value":
#                 v.click()
#
#     def Mouse(self, locator):
#         webelement = self.search_element(locator)
#         self.action.move_to_element(webelement).perform()
#         self.action.context_click(webelement).perform()
#         self.action.drag_and_drop(webelement, webelement).perform()
#         self.action.click_and_hold(webelement).release().perform()
#         self.action.drag_and_drop_by_offset(webelement, 100, 0).perform()
#         self.action.double_click(webelement).perform()
#
#     def keybord(self, locator):
#         element = self.search_element(locator)
#         self.action.key_down(Keys.CONTROL).send_keys('a').send_keys('c').perform()
#         sleep(2)
#         self.action.key_down(Keys.TAB).send_keys('v').perform()
#         sleep(5)
#         self.action.scroll_by_amount(30, 100).perform()
#         sleep(3)
#         self.action.scroll_to_element(element).perform()
#
#     def pops(self):
#         pop = self.driver.switch_to.alert
#         pop.accept()
#         sleep(2)
#         pop.dismiss()
#         sleep(3)
#         pop.send_keys('value')
#
#     def frames(self, locator, locator1):
#         webelement = self.search_element(locator)
#         self.driver.switch_to.frame('name')
#         self.driver.switch_to.frame(webelement)
#         element = self.search_element(locator1)
#         element.click()
#         self.driver.switch_to.parent_frame()
#         sleep(3)
#         self.driver.switch_to.default_content()
#
#     def windows(self):
#         current = self.driver.current_window_handle
#         windows_ids = self.driver.window_handles
#         for id in windows_ids:
#             self.driver.switch_to.window(id)
#             if self.driver.title == "facebook" or self.driver.current_url == ".com":
#                 self.driver.close()
#
#     def webtables(self, row, col):
#         rows = self.search_elements(row)
#         cols = self.search_elements(col)
#         count=0
#         class mahe(Exception):
#             ...
#         try:
#             for r in range(2, len(rows) + 1):
#                 for c in range(1, len(cols) + 1):
#                     if r == 140:
#                         dat=self.driver.find_element('xpath',f'//table[@id="countries"]/tbody/tr[{r}]/td[{c}]').text
#                         print(dat)
#                     else:
#                         country = self.driver.find_element('xpath',
#                                                            f'//table[@id="countries"]/tbody/tr[{r}]/td[2]/strong').text
#                         data = self.driver.find_element('xpath',
#                                                         f'//table[@id="countries"]/tbody/tr[{r}]/td[2]/strong/../../td[{c}]').text
#                         print("Country-->", country, "#-->", data)
#                 print()
#         except:
#             raise mahe
#
#     def calender(self):
#         month_t = 'Jun'
#         year_t = '1998'
#         date = '11'
#         while True:
#             m = self.driver.find_element('xpath', 'xpath-value').text
#             y = self.driver.find_element('xpath', 'xpath-value').text
#             if m == month_t and y == year_t:
#                 break
#             else:
#                 next = self.driver.find_element('xpath', 'next_btn_xpath').click()
#         Dates = self.driver.find_elements('xpath', 'xpath-value')
#         for i in Dates:
#             if i.text == date:
#                 i.click()
#                 break


from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from time import sleep


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def search_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def search_elements(self, locator):
        elements=WebDriverWait(self.driver,10,poll_frequency=0.4,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,
                                                                                     ElementNotSelectableException,Exception]).until(
            e.visibility_of_all_elements_located(locator)
        )
        return elements
        # elements = self.driver.find_elements(*locator)
        # return elements

    def click(self, locator):
        ele = self.search_element(locator)
        ele.click()

    def send_data(self, locator, data):
        el = self.search_element(locator)
        el.send_keys(data)

    def drop_down(self, locator):
        drop = Select(self.search_element(locator))
        drop.select_by_index(1)
        drop.select_by_value(value='mahesh')
        drop.select_by_visible_text('mahesh')
        v = drop.options
        for i in v: 
            if i.text == 'mahesh':
                i.click()
        drop.deselect_all()
        drop.deselect_by_value(value='rony')
        drop.deselect_by_index(3)
        drop.deselect_by_visible_text("rony")
        print(drop.first_selected_option)
        print(drop.all_selected_options)
        print(drop.is_multiple)

    def screenshots(self, locator):
        self.driver.save_screenshot()
        self.driver.get_screenshot_as_png('amhesh')

    def Mouse(self, locator):
        webelement = self.search_element(locator)
        self.action.move_to_element(webelement).perform()
        self.action.double_click(webelement).perform()
        self.action.context_click(webelement).perform()
        self.action.drag_and_drop(webelement, webelement).perform()
        self.action.click_and_hold(webelement).release(webelement).perform()

    def keyborad(self, locator):
        web = self.search_element(locator)
        self.action.key_down(Keys.ARROW_UP).send_keys('a').perform()
        self.action.key_up(Keys.ARROW_UP).perform()

    def pops(self):
        pop = self.driver.switch_to.alert
        pop.accept()
        pop.dismiss()
        pop.send_keys('mahesh')

    def frames(self, locator):
        web = self.search_element(locator)
        self.driver.switch_to.frame('id')
        self.driver.switch_to.frame('name')
        self.driver.switch_to.frame(web)
        sleep(2)
        self.driver.switch_to.parent_frame()
        sleep(3)
        self.driver.switch_to.default_content()

    def window_handle(self):
        current = self.driver.current_window_handle
        ids = self.driver.window_handles
        for i in ids:
            self.driver.switch_to.window(i)
            if self.driver.title == 'mahesh':
                self.driver.close()

    def webtables(self,row,col):
        rows = self.search_elements(row)
        cols = self.search_elements(col)

        for r in range(1, len(rows) + 1):
            for c in range(1, len(cols) + 1):
                data = self.driver.find_element('xpath', f'//table[@id="countries"]/tbody/tr[{r}]/td[{c}]').text
                print(data)

    def calender(self):
        month = ''
        year = ''
        date = ''
        while True:
            month = self.driver.find_element('xpath', '').text
            year = self.driver.find_element('xpath', '').text
            if month == month and year == year:
                break
            else:
                self.driver.find_element('xpath', '').click()
        dates=self.driver.find_elements('xpath','')
        for d in dates:
            if d.text==date:
                d.click()
                break
