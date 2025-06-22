from selenium.common import NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver import ActionChains, Keys
from time import sleep


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def search_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def search_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    def click(self, locator):
        # Explicit Timeout
        ele = WebDriverWait(self.driver, 10, poll_frequency=0.2,
                            ignored_exceptions=[NoSuchElementException, ElementNotSelectableException,
                                                ElementNotVisibleException, Exception]).until(
            e.presence_of_element_located(('id', 'female'))
        )
        ele.click()

    def click1(self, locator):
        # Explicit Timeout
        ele = WebDriverWait(self.driver, 10, poll_frequency=0.2,
                            ignored_exceptions=[NoSuchElementException, ElementNotSelectableException,
                                                ElementNotVisibleException, Exception]).until(
            e.presence_of_element_located(('xpath', '//input[@id="datepicker"]'))
        )
        ele.click()

    def click_common(self, locator):
        click_action = self.search_element(locator)
        click_action.click()

    def send_data(self, locator, text):
        ele = self.search_element(locator)
        ele.send_keys(text)

    def Days_selection(self, locator):
        eles = self.search_elements(locator)
        for ele in eles:
            if ele.text == "Monday" or ele.text == 'Wednesday' or ele.text == 'Friday':
                ele.click()

    def drop(self, locator):
        ele = Select(self.search_element(locator))
        # ele.select_by_index(0)
        ele.select_by_value("germany")
        # ele.select_by_visible_text("Green")
        #
        # #DESELECT
        # ele.deselect_by_visible_text(text)
        # ele.deselect_all()
        # ele.deselect_by_index(3)
        # ele.deselect_by_value("value")

    def drop_colours(self, locator):
        c = Select(self.search_element(locator))
        #OPTIONS:
        items = c.options
        for i in items:
            if i.text == "Red" or i.text == "Green":
                i.click()
        f = c.first_selected_option  #webelemt
        print((f))
        f_all = c.all_selected_options  #webelements
        print(f_all)
        print(c.is_multiple)
    def calender(self, next_locator):
        month_data = "September"
        year_data = "2027"
        date = "23"
        while True:
            month = self.driver.find_element('xpath', '//span[@class="ui-datepicker-month"]').text
            year = self.driver.find_element('xpath', '//span[@class="ui-datepicker-year"]').text
            if month_data == month and year_data == year:
                break
            else:
                self.search_element(next_locator).click()

        dates = self.driver.find_elements('xpath', '//table[@class="ui-datepicker-calendar"]/tbody/tr/td/a')
        for d in dates:
            if d.text == date:
                d.click()
                break

    def webtable(self):
        rows = self.driver.find_elements('xpath', '//table[@name="BookTable"]/tbody/tr')
        cols = self.driver.find_elements('xpath', '//table[@name="BookTable"]/tbody/tr/th')
        for r in range(2, len(rows) + 1):
            for c in range(1, len(cols) + 1):
                data = self.driver.find_element('xpath', f'//table[@name="BookTable"]/tbody/tr[{r}]/td[{c}]').text
                print(data)
            print()

    def dynamic_web(self, rows_locator, cols_locator):
        rows = self.search_elements(rows_locator)
        cols = self.search_elements(cols_locator)
        for r in range(1, len(rows) + 1):
            for c in range(1, len(cols) + 1):
                data = self.driver.find_element("xpath", f'//table[@id="taskTable"]/tbody/tr[{r}]/td[{c}]').text
                print(data)
            print()

    def check_boxes_table(self):
        devices_name = self.driver.find_elements('xpath', '//table[@id="productTable"]/tbody/tr/td[2]')
        devices = []
        for item in devices_name:
            devices.append(item.text)
        print(devices)
        for i in devices:
            if i == "Laptop" or i == "Smartwatch" or i == "Wireless Earbuds":
                self.driver.find_element('xpath',
                                         f'//table[@id="productTable"]/tbody/tr/td[text()="{i}"]/../td[4]/input').click()

    def Mouseactions(self, locator):
        ele = self.search_element(locator)
        self.actions.move_to_element(ele).perform()  #mousehovering
        self.actions.context_click(ele).perform()   #right click
        self.actions.double_click(ele).perform()  #double click
        s = self.search_element(locator)
        self.actions.drag_and_drop(s, ele).perform()  #drag and drop
        self.actions.drag_and_drop_by_offset(ele, 100, 200).perform()  #drag_and_drop_by_offset
        self.actions.click_and_hold(ele).release(ele).perform()  #click and hold
        self.actions.click(ele)  #click

    def key_boardactions(self, locator):
        ele = self.search_element(locator)
        self.actions.key_down(Keys.CONTROL).send_keys('a').send_keys("c").key_up(Keys.CONTROL).perform()
        sleep(1)
        self.actions.send_keys(Keys.TAB).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        sleep(2)
        # self.actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        sleep(2)

    def alerts(self, text):
        pop = self.driver.switch_to.alert
        pop.accept()
        sleep(2)
        pop.dismiss()
        t = pop.text
        print(t)
        pop.send_keys(text)

    def frames(self, locator):
        self.driver.switch_to.frame(self.search_element(locator))  #webelement
        self.driver.switch_to.frame('name')
        self.driver.switch_to.frame('id')

        self.driver.switch_to.default_content()
        self.driver.switch_to.parent_frame()

    def windows(self):
        c = self.driver.current_window_handle
        print(c)
        multiple = self.driver.window_handles
        for win in multiple:
            self.driver.switch_to.window(win)
            if self.driver.title == "Mahesh Babu - Wikipedia" or self.driver.current_url == "https://testautomationpractice.blogspot.com/feeds/posts/default" or self.driver.current_url=="https://demo.opencart.com/":
                self.driver.close()
                sleep(3)





