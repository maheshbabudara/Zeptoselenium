from Lib.library import Base
from Utilities.Locator import demo_locators
from time import sleep

class test(Base):
    def det(self,name,email,phno,address):
        self.send_data(demo_locators.name_locator,name)
        sleep(1)
        self.send_data(demo_locators.email_locator,email)
        sleep(1)
        self.send_data(demo_locators.phn_locator,phno)
        sleep(1)
        self.send_data(demo_locators.address_locator,address)
        sleep(1)
        self.click(demo_locators.gender_locator)
        sleep(1)
        self.click(demo_locators.sunday_locator)
        sleep(1)
        self.click(demo_locators.tuesday_locator)
        sleep(1)
        self.click(demo_locators.friday_locator)
        sleep(2)
    def drop_down(self):
        self.drop(demo_locators.country_drp)
        sleep(4)
        self.drop_colours(demo_locators.colours)
        sleep(2)
    def calender(self):
        self.click(demo_locators.datepicker_locator)
        sleep(1)
        self.date_calen(demo_locators.Dates_locator,demo_locators.next_locator,demo_locators.prev_locator,demo_locators.month_locator,demo_locators.year_locator)
        sleep(1)
        # self.click(demo_locators.orange_hrm)
        # sleep(1)
        # self.driver.back()
        # sleep(1)
    def switch_window(self):
        print('before swithcing')
        self.click(demo_locators.posts_locator)
        sleep(1)
        self.window()
        sleep(2)
        print('swithed abnd currently in switched page')
        # self.driver.switch_to.default_content()
        # print('came to default page')
        sleep(4)
    def web(self):
        self.web_table(demo_locators.loc_rows,demo_locators.loc_cols)

    def condition_based_data(self):
        self.web_condition(demo_locators.subject_locator)
    def chek(self):
        self.device_check(demo_locators.device_Names)

    def pops(self,data):
        self.click(demo_locators.accept_locator)
        sleep(1)
        self.alerts_accept()
        sleep(1)
        self.click(demo_locators.confirm_locator)
        sleep(1)
        self.alerts_accept()
        sleep(1)
        self.click(demo_locators.prompt_locator)
        sleep(1)
        self.alerts_sendtext(data)
    def ACTIONS(self):
        self.actions(demo_locators.doubleclick_locator)

    def fames(self,data,pwd,cpwd):
        self.driver.get("https://demoapps.qspiders.com/ui/frames/nested?sublist=1")
        sleep(1)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        sleep(1)
        self.frames(demo_locators.first_frame,demo_locators.second_frame)
        sleep(2)
        self.send_data(demo_locators.frame_email,data)
        sleep(1)
        self.send_data(demo_locators.frame_pwd,pwd)
        sleep(1)
        self.send_data(demo_locators.frame_cpwd,cpwd)
        sleep(1)
        self.driver.switch_to.parent_frame()
        print('switched to parent frame')
        sleep(1)
        self.driver.switch_to.default_content()
        sleep(1)
        self.driver.find_element('xpath',"//section[text()='Mouse Actions']").click()
        sleep(1)
        self.driver.find_element('xpath',"//section[text()='Drag & Drop']").click()
        sleep(1)










