# from Lib.lib2 import Base
# from time import sleep
# from Utilities.Blog_locators import locators
#
# class Blog_practise(Base):
#     def practise(self,name,email):
#         self.send_data(locators.Name_locator,name)
#         sleep(2)
#         self.send_data(locators.Email_locator,email)
#         sleep(2)
#         self.keys_action()
#         sleep(1)
#         self.keys_action()
#         sleep(2)
#         self.drop(locators.country_locator)


from Lib.lib2 import Base
from Utilities.Blog_locators import locators
from time import sleep

class utube(Base):
    def tube(self,data):
        self.send_data(locators.search_box,data)
        sleep(1)
        self.click(locators.search)
        sleep(2)

